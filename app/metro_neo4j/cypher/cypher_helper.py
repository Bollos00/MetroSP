import os

class CypherHelper:
    def __init__(self, t_train_trip=150, t_boarding=10, t_wait_train=300, v_ped=1.0, d_diloc=100):
        abs_dir_path = os.path.dirname(os.path.abspath(__file__))
        with open(f'{abs_dir_path}/create_nodes.cypher', 'r') as f:
            self.create_nodes = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_boarding_names.cypher', 'r') as f:
            self.create_bd_names = CypherHelper.cypher_optimized(f.read())
        
        with open(f'{abs_dir_path}/create_relationships_entry.cypher', 'r') as f:
            self.create_rl_entry = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_relationships_exit.cypher', 'r') as f:
            self.create_rl_exit = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_relationships_train_way_minus.cypher', 'r') as f:
            self.create_rl_train_way_minus = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_relationships_train_way_plus.cypher', 'r') as f:
            self.create_rl_train_way_plus = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_relationships_transfer.cypher', 'r') as f:
            self.create_rl_transfer = CypherHelper.cypher_optimized(f.read())
        
        with open(f'{abs_dir_path}/dijkstra.cypher', 'r') as f:
            self.dijkstra = CypherHelper.cypher_optimized(f.read())

        with open(f'{abs_dir_path}/get_relationship_id_from_nodes_ids.cypher', 'r') as f:
            self.relationship_id_from_nodes_ids = CypherHelper.cypher_optimized(f.read())
    
        with open(f'{abs_dir_path}/get_stations.cypher', 'r') as f:
            self.stations = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/get_station_id.cypher', 'r') as f:
            self.station_id = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/get_station_lines.cypher', 'r') as f:
            self.station_lines = CypherHelper.cypher_optimized(f.read())

        with open(f'{abs_dir_path}/update_rl_time_from_id.cypher', 'r') as f:
            self.update_rl_time_from_id = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/update_rl_time_from_node_ids.cypher', 'r') as f:
            self.update_rl_time_from_node_ids = CypherHelper.cypher_optimized(f.read())

        with open(f'{abs_dir_path}/get_rls_from_ids.cypher', 'r') as f:
            self.rls_from_ids = CypherHelper.cypher_optimized(f.read())

        t_disloc_train  = int(t_train_trip + t_boarding)
        t_disloc_transf = int(v_ped*d_diloc + t_wait_train/2 + t_boarding)
        t_disloc_exit   = int(v_ped*d_diloc)
        t_disloc_entry  = int(v_ped*d_diloc + t_wait_train/2 + t_boarding)

        self.create_rl_entry = self.create_rl_entry.replace(
            "$$defaulttime$$", str(t_disloc_entry)
        )
        self.create_rl_exit = self.create_rl_exit.replace(
            "$$defaulttime$$", str(t_disloc_exit)
        )
        self.create_rl_train_way_minus = self.create_rl_train_way_minus.replace(
            "$$defaulttime$$", str(t_disloc_train)
        )
        self.create_rl_train_way_plus = self.create_rl_train_way_plus.replace(
            "$$defaulttime$$", str(t_disloc_train)
        )
        self.create_rl_transfer = self.create_rl_transfer.replace(
            "$$defaulttime$$", str(t_disloc_transf)
        )

    @staticmethod
    def cypher_optimized(cypher_code):
        return cypher_code
    
    def get_dijkstra(self, start, end, paths_count, default_weight):
        return self.dijkstra.replace(
            "$$start$$", str(start)
        ).replace(
            "$$end$$", str(end)
        ).replace(
            "$$defaultweight$$", str(default_weight)
        ).replace(
            "$$paths_count$$", str(paths_count)
        )
    
    def get_relationship_id_from_nodes_ids(self, start_id, end_id):
        return self.relationship_id_from_nodes_ids.replace(
            "$$start_id$$", str(start_id)
        ).replace(
            "$$end_id$$", str(end_id)
        )
    
    def get_stations(self):
        return self.stations
    
    def get_station_id(self, station):
        return self.station_id.replace(
            "$$station$$", station
        )
    
    def get_station_lines(self, station):
        return self.station_lines.replace(
            "$$station$$", station
        )

    def get_update_rl_time_from_id(self, rl_id, rl_time):
        return self.update_rl_time_from_id.replace(
            "$$id$$", str(rl_id)
        ).replace(
            "$$time$$", str(rl_time)
        )

    def get_update_rl_time_from_node_ids(self, start_node, end_node, rl_time):
        return self.update_rl_time_from_node_ids.replace(
            "$$start_node$$", str(start_node)
        ).replace(
            "$$end_node$$", str(end_node)
        ).replace(
            "$$time$$", str(rl_time)
        )
        
    def get_rls_from_ids(self, ids):
        return self.rls_from_ids.replace(
            "$$relationhip_ids$$", str(ids)
        )
    
    def get_node_id_0(self):
        return "MATCH(n) WHERE id(n)=0 RETURN n"
        
if __name__ == "__main__":
    ch = CypherHelper()