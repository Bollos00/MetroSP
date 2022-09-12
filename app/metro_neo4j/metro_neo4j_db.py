import neo4j
import os
import time
from .credentials import credentials
from .cypher.cypher_helper import CypherHelper

class MetroNeo4jDatabase(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            uri = credentials.NEO4J_URI
            user = credentials.NEO4J_USER
            password = credentials.NEO4J_PASSWORD
            cls._instance = super(MetroNeo4jDatabase, cls).__new__(cls)
            cls._init(cls)
        return cls._instance

    def _init(cls):
        cls.helper = CypherHelper(60)
        uri = credentials.NEO4J_URI
        user = credentials.NEO4J_USER
        password = credentials.NEO4J_PASSWORD
        
        while True:
            try:
                cls.driver = neo4j.GraphDatabase.driver(uri, auth=(user, password))
                cls.query(cls, cls.helper.get_node_id_0())
            except Exception as e:
                # print("Failed to create the driver:", e)
                # print("Trying again in 1 second.")
                time.sleep(1)
            else:
                # print("Ok!")
                break

    def close(self):
        self.driver.close()

    def query(self, query):
        assert self.driver is not None, "Driver not initialized!"
        
        response = None

        with self.driver.session() as session:        
            response = list(session.run(query))
        
        return response
    
    def delete_detach(self):
        self.query("MATCH (n) DETACH DELETE n")

    def reset(self):
        ok = None
        while not ok:
            self.delete_detach()
            
            self.query(self.helper.create_nodes)
            self.query(self.helper.create_bd_names)
            
            self.query(self.helper.create_rl_entry)
            self.query(self.helper.create_rl_exit)
            self.query(self.helper.create_rl_train_way_minus)
            self.query(self.helper.create_rl_train_way_plus)
            self.query(self.helper.create_rl_transfer)
            ok = self.query(self.helper.get_node_id_0())
        
    def dijkstra(self, start, end, paths=1, default_weight=1000):
        return self.query(self.helper.get_dijkstra(start, end, paths, default_weight))
    
    def get_relationship_id_from_nodes_ids(self, start_id, end_id):
        return self.query(self.helper.get_relationship_id_from_nodes_ids(
            start_id, end_id
        ))

    def get_stations(self):
        return self.query(self.helper.get_stations())
    
    def get_station_lines(self, station):
        return self.query(self.helper.get_station_lines(station))
    
    def update_rl_time_from_id(self, rl_id, rl_time):
        return self.query(self.helper.update_rl_time_from_id(rl_id, rl_time))
    
    def get_graph_nodes(self):
        return self.query("MATCH (n) RETURN n")
    
    def get_graph_relationships(self):
        return self.query("MATCH ()-[r]->() RETURN r")
    