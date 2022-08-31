import neo4j
import os
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

    def _init(self):
        self.helper = CypherHelper(60)
        uri = credentials.NEO4J_URI
        user = credentials.NEO4J_USER
        password = credentials.NEO4J_PASSWORD
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

    def reset(self):
        self.delete_detach()
        
        self.query(self.helper.create_nodes)
        self.query(self.helper.create_bd_names)
        
        self.query(self.helper.create_rl_entry)
        self.query(self.helper.create_rl_exit)
        self.query(self.helper.create_rl_train_way_minus)
        self.query(self.helper.create_rl_train_way_plus)
        self.query(self.helper.create_rl_transfer)
        
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