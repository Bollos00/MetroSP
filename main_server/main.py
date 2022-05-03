import neo4j
import os

from cypher.cypher_helper import CypherHelper
from credentials import credentials

class MetroDatabase:

    def __init__(self, uri, user, password):
        try:
            self.driver = neo4j.GraphDatabase.driver(uri, auth=(user, password))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def query(self, query, db=None):
        assert self.driver is not None, "Driver not initialized!"
        
        session = None
        response = None
        
        try: 
            session = self.driver.session() if db is None else self.driver.session(database=db)
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response
    
    def delete_detach(self):
        self.query("MATCH (n) DETACH DELETE n")

    def reset(self, helper):
        self.delete_detach()
        self.query(helper.create_nodes)
        self.query(helper.create_rl_board)
        self.query(helper.create_rl_station)
        self.query(helper.create_rl_v1)
        self.query(helper.create_rl_v2)

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


def init_driver():
    uri = credentials.NEO4J_URI
    user = credentials.NEO4J_USER
    password = credentials.NEO4J_PASSWORD

    return MetroDatabase(uri, user, password)


if __name__ == "__main__":

    driver = init_driver()

    helper = CypherHelper(60)
    
    # driver.reset(helper)

    print(driver.update_tr_time(helper, l=2, v=1, n=1, time=39))
    print(driver.update_ft_transf_time(helper, "Ana Rosa", fl=1, fv=1, tl=2, tv=2, time=40))
    print(driver.update_ft_plat_bd_time(helper, "Ana Rosa", tl=2, tv=2, time=40))
    print(driver.update_ft_bd_plat_time(helper, "Ana Rosa", fl=1, fv=1, time=40))

    driver.close()