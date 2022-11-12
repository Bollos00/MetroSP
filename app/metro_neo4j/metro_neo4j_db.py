import neo4j
import os
import time
from . import credentials
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
                with cls.driver.session() as session:
                    cls.query(cls, session, cls.helper.get_node_id_0())
            except Exception as e:
                # print("Failed to create the driver:", e)
                # print("Trying again in 1 second.")
                time.sleep(1)
            else:
                # print("Ok!")
                break

    @staticmethod
    def get_session():
        session = MetroNeo4jDatabase().driver.session()
        try:
            yield session
        finally:
            session.close()

    def close(self):
        self.driver.close()

    def query(self, session, query):
        return list(session.run(query))
    
    def reset(self):
        ok = None
        while not ok:
            session = self.driver.session()
            self.query(session, "MATCH (n) DETACH DELETE n")
            
            self.query(session, self.helper.create_nodes)
            self.query(session, self.helper.create_bd_names)
            
            self.query(session, self.helper.create_rl_entry)
            self.query(session, self.helper.create_rl_exit)
            self.query(session, self.helper.create_rl_train_way_minus)
            self.query(session, self.helper.create_rl_train_way_plus)
            self.query(session, self.helper.create_rl_transfer)
            ok = self.query(session, self.helper.get_node_id_0())
            session.close()
        
    def dijkstra(self, session, start, end, paths=1, default_weight=1000):
        return self.query(
            session, self.helper.get_dijkstra(start, end, paths, default_weight)
        )
    
    def get_relationship_id_from_nodes_ids(self, session, start_id, end_id):
        rl = self.query(
            session, self.helper.get_relationship_id_from_nodes_ids(
                start_id, end_id
            )
        )
        
        return None if len(rl) != 1 else rl[0][0].id

        
    def get_rl_time_from_ids(self, session, ids):
        ids_str = '[{}]'.format(','.join([str(id) for id in ids]))
        records = self.query(session, self.helper.get_rls_from_ids(ids_str))
        rl_times = dict()
        for record in records:
            rl = record[0]
            rl_times[rl.id] = rl.get("time")
        return rl_times
    
    def get_rl_time_from_node_ids(self, session, node_ids):
        rl_ids = dict()
        for n in node_ids:
            rl = self.get_relationship_id_from_nodes_ids(
                session, n[0], n[1]
            )
            if rl is not None:
                rl_ids[rl] = n
        times = self.get_rl_time_from_ids(session, rl_ids.keys())
        return {rl_ids[rl]: times[rl] for rl in rl_ids.keys()}

    def get_stations(self, session):
        return self.query(session, self.helper.get_stations())
    
    def get_station_id(self, session, station):
        id = self.query(session, self.helper.get_station_id(station))
        if len(id) != 1:
            return None
        return id[0].get('id(n)')

    def get_station_lines(self, session, station):
        lines = self.query(session, self.helper.get_station_lines(station))
        return [l.get("b.l") for l in lines]
    
    def update_rl_time_from_id(self, session, rl_id, rl_time):
        return self.query(session, self.helper.get_update_rl_time_from_id(rl_id, rl_time))
    
    def update_rl_time_from_node_ids(self, session, id_times):
        for rl_id, rl_time in id_times.items():
            self.query(session, self.helper.get_update_rl_time_from_node_ids(
                rl_id[0], rl_id[1], rl_time
            ))
    
    def get_graph_nodes(self, session):
        return self.query(session, "MATCH (n) RETURN n")
    
    def get_graph_relationships(self, session):
        return self.query(session, "MATCH ()-[r]->() RETURN r")
    