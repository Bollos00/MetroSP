import numpy
import datetime
from metro_neo4j.metro_neo4j_db import MetroNeo4jDatabase
from metro_sql import sql_helper, models
from scipy.stats import linregress


class NodeLinkUpdater:
    INITIAL_DELAY = datetime.timedelta(seconds=5).seconds
    UPDATE_PERIOD = datetime.timedelta(seconds=60)
    UPDATE_LIMIT_TIME = datetime.timedelta(minutes=2, seconds=30)

    OUTLIER_FILTER_N = 1.5
    OUTLIER_FILTER_SAMPLES_PER_SPLIT = 10
    OUTLIER_FILTER_MAX_SPLITS = 4
    
    CONFIDENCE_SAMPLES_COUNT = 20

    # def __init__(self, sample0, samples, t_end):
    #     self.sample0 = sample0
    #     self.samples = samples
    #     self.t_end = t_end


    @staticmethod
    def update_node_links_table(neo4jdb, sqldb):
        nodes = sql_helper.get_users_with_nodes(sqldb)
        node_links = list()
        nodes_to_delete = list()
        for u in nodes.keys():
            user_nodes = nodes[u]
            for i in range(len(user_nodes)-1):
                start_node = user_nodes[i]
                nodes_to_delete.append(start_node)
                end_node = user_nodes[i+1]
                rl = MetroNeo4jDatabase().get_relationship_id_from_nodes_ids(
                    neo4jdb, start_node.node_id, end_node.node_id
                )
                if rl is None:
                    continue
                disp_time = int((
                    end_node.date_time - start_node.date_time
                ).total_seconds())
                node_links.append(models.NodeLink(
                    node_link_id=rl,
                    start_date_time=start_node.date_time,
                    end_date_time=end_node.date_time,
                    displacement_time_s = disp_time             
                ))
        sql_helper.delete_nodes(sqldb, nodes_to_delete)
        sql_helper.create_node_links(sqldb, node_links)
        
        
    @staticmethod
    def update_node_links_graph(neo4jdb, sqldb):
        # Inicialmente atualiza a tabela com os tempos de deslocamento
        NodeLinkUpdater.update_node_links_table(neo4jdb, sqldb)
        
        node_links = sql_helper.get_users_with_node_links(
            sqldb, NodeLinkUpdater.UPDATE_LIMIT_TIME
        )

        t_end = datetime.datetime.now()
        t_begin = (t_end - NodeLinkUpdater.UPDATE_LIMIT_TIME).timestamp()
        # t_0 = (t_end - NodeLinkUpdater.UPDATE_PERIOD).timestamp()
        # t_0 -= t_begin
        t_end = t_end.timestamp() - t_begin
        
        current_nl_times = MetroNeo4jDatabase().get_rl_time_from_ids(
            neo4jdb, node_links.keys()
        )
        
        ids_times = dict()
        
        for nl_id, samples in node_links.items():
            disp_time0 = current_nl_times.get(nl_id, 250)
            # sample0 = (t_0, disp_time0)
            sample0 = (0, disp_time0)
            samples = numpy.array(samples)
            samples[:, 0] -= t_begin
            updated_time = int(.5 + NodeLinkUpdater.solve(sample0, samples, t_end))
            if not numpy.isnan(updated_time):
                ids_times[nl_id] = updated_time
            
        MetroNeo4jDatabase().update_rl_time_from_ids(neo4jdb, ids_times)


    @staticmethod
    def _remove_outfiles_single(s):
        values = s[:, 1]
        avg_values = numpy.average(values)
        std_values = numpy.std(values)
        return s[numpy.abs(s[:, 1] - avg_values) < NodeLinkUpdater.OUTLIER_FILTER_N*std_values]


    @staticmethod
    def remove_outliers(samples):
        # quantidade de subamostras
        splits = int(numpy.min(
            [
                1 + samples.shape[0]/NodeLinkUpdater.OUTLIER_FILTER_SAMPLES_PER_SPLIT,
                NodeLinkUpdater.OUTLIER_FILTER_MAX_SPLITS
            ]
        ))
        subsamples = numpy.array_split(samples, splits)
        for i, s in enumerate(subsamples):
            subsamples[i] = NodeLinkUpdater._remove_outfiles_single(s)
        return numpy.vstack(subsamples)


    @staticmethod
    def linear_regression_origin_intercept(samples):
        # Retorna o coefieciente da regressão linear que passa pela origem
        x = samples[:, 0]
        y = samples[:, 1]
        return numpy.sum(x*y)/numpy.sum(x*x)


    @staticmethod
    def linear_regression_point_intercept(sample0, samples):
        # Retorna os coefiecientes da regressão linear que passa por sample0
        norm_samples = samples - sample0
        a = NodeLinkUpdater.linear_regression_origin_intercept(norm_samples)
        if samples.shape[0] < NodeLinkUpdater.CONFIDENCE_SAMPLES_COUNT:
            a *= samples.shape[0]/NodeLinkUpdater.CONFIDENCE_SAMPLES_COUNT
        b = sample0[1] - a*sample0[0]
        return a, b


    @staticmethod
    def solve(sample0, samples, t_end):
        samples = NodeLinkUpdater.sort_samples(samples)
        samples = NodeLinkUpdater.remove_outliers(samples)
        if samples.size == 0:
            return sample0[1]
        # sample0 é o par de coordenadas da predição anterior (em t=t0)
        # As amostras são normalizados para plotar uma reta que passa
        #  por sample0 
        lr = linregress(samples)
        result = NodeLinkUpdater._linear_regression_predict(lr.slope, lr.intercept)
        # a, b = NodeLinkUpdater.linear_regression_point_intercept(sample0, samples)
        a, b = NodeLinkUpdater.linear_regression_point_intercept(
            sample0, [t_end, result]
        )
        result = NodeLinkUpdater._linear_regression_predict(a, b, t_end)
        return sample0[1] if numpy.isnan(result) else result


    @staticmethod
    def _linear_regression_predict(a, b, x):
        return b + a*x


    @staticmethod
    def sort_samples(samples):
        # Sort array by time (dimensions 0)
        return numpy.array(sorted(samples, key=lambda s: s[0]))
