import neo4j
import os
from cypher.cypher_helper import CypherHelper

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

def init_driver():
    uri = os.getenv("NEO4J_URI", None)
    user = os.getenv("NEO4J_USER", None)
    password = os.getenv("NEO4J_PASSWORD", None)

    if None in [uri, user, password]:
        print("""Error! Environment variables "NEO4J_URI", "NEO4J_USER" and "NEO4J_PASSWORD"
        need to be set.
        """)
        exit(1)

    return MetroDatabase(uri, user, password)


if __name__ == "__main__":

    driver = init_driver()

    helper = CypherHelper(60)
    
    driver.reset(helper)
    
    print(driver.query("MATCH (n:Station{name:'Jabaquara'}) RETURN n"))

    driver.close()