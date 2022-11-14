import string
import secrets
import uuid
import requests
import json
import datetime
import numpy

ADDRES = "https://app-bollos00.cloud.okteto.net"
ADDRES = "http://0.0.0.0:8080"

def random_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(chars) for i in range(length))

class Relationship:
    def __init__(self, start, end, time):
        self.start = start
        self.end = end
        self.time = time

class Node:
    def __init__(self, id, time):
        self.id = id
        self.time = time
    
def relationships_from_nodes(nodes: list[Node]):
    rls = list()
    for i in range(len(nodes) - 1):
        rls.append(Relationship(nodes[i].id, nodes[i+1].id, nodes[i+1].time))
    return rls

class UserClient:
           
    def __init__(self):
        self.id = uuid.uuid4()
        self.password = random_password()
        self.deviation_time_rand = .3
        
    def register(self):
        url = ADDRES + "/create_user"
        payload = json.dumps({
            'id': str(self.id),
            'password': self.password
        }, indent=2)
        
        r = requests.post(url, data=payload)
    
    
    def unregister(self):
        url = ADDRES + "/delete_user"
        payload = json.dumps({
            'id': str(self.id),
            'password': self.password
        }, indent=2)
        
        r = requests.post(url, data=payload)

    def pre_process_nodes(self, nodes):
        nodes.reverse()
        total_time = 0
        for i, n in enumerate(nodes):
            node_time = n.time*numpy.random.normal(1, self.deviation_time_rand)
            nodes[i].time = datetime.timedelta(seconds=total_time)
            total_time -= node_time
        nodes.reverse()
        return nodes
    
    def relationship(self, rl: Relationship):
        nodes = [Node(rl.start, 0), Node(rl.end, rl.time)]
        return self.route(nodes)
    
    def route(self, nodes):
        nodes = self.pre_process_nodes(nodes)
        now = datetime.datetime.utcnow()
        
        for i, n in enumerate(nodes):
            nodes[i] = {
                "node_id": n.id,
                "date_time": str(now + n.time)
            }
            
        payload = json.dumps({
            "nodes": nodes,
            "user": {
                'id': str(self.id),
                'password': self.password
            }
        }, indent=2)
        url = ADDRES + "/create_nodes"

        r = requests.post(url, data=payload)
        print(payload)

        
if __name__ == "__main__":
    def nodes_sacoma_oratorio():
        return [
            Node(110, 0),
            Node(112, 300),
            Node(115, 200),
            Node(118, 220),
            Node(120, 500),
            Node(242, 150),
            Node(240, 60),
        ]

    N = 2
    for i in range(N):
        rls = relationships_from_nodes(nodes_sacoma_oratorio())
        for rl in rls:
            u = UserClient()
            u.register()
            u.relationship(rl)
            # u.unregister()