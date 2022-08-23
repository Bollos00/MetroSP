import neo4j
import os

class MetroDatabaseDriver:

    def __init__(self, uri, user, password):
        try:
            self.driver = neo4j.GraphDatabase.driver(uri, auth=(user, password))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def query(self, query):
        assert self.driver is not None, "Driver not initialized!"
        
        response = None

        with self.driver.session() as session:        
            response = list(session.run(query))
        
        return response
    
    def delete_detach(self):
        self.query("MATCH (n) DETACH DELETE n")

    def reset(self, helper):
        self.delete_detach()
        
        self.query(helper.create_nodes)
        self.query(helper.create_bd_names)
        
        self.query(helper.create_rl_entry)
        self.query(helper.create_rl_exit)
        self.query(helper.create_rl_train_way_minus)
        self.query(helper.create_rl_train_way_plus)
        self.query(helper.create_rl_transfer)
        
    def dijkstra(self, helper, start, destiny, default_weight=1000, paths=1):
        return self.query(helper.get_dijkstra(start, destiny, default_weight, paths))
    
    def update_tr_time(self, helper, l, v, n, time):
        return self.query(helper.get_update_tr_time(l, v, n, time))

    def update_ft_transf_time(self, helper, station, fl, fv, tl, tv, time):
        return self.query(helper.get_update_ft_transf_time(station, fl, fv, tl, tv, time))

    def update_ft_bd_plat_time(self, helper, station, fl, fv, time):
        return self.query(helper.get_update_ft_bd_plat_time(station, fl, fv, time))

    def update_ft_plat_bd_time(self, helper, station, tl, tv, time):
        return self.query(helper.get_update_ft_plat_bd_time(station, tl, tv, time))