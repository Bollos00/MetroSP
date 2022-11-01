import string
import secrets
import uuid
import requests
import json
import datetime
import numpy

ADDRES = "http://127.0.0.1:8000"

def random_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(chars) for i in range(length))

class UserClient:
    class Node:
        def __init__(self, id, time):
            self.id = id
            self.time = time
        
    def __init__(self):
        self.id = uuid.uuid4()
        self.password = random_password()
        self.deviation_time_rand = 30
        
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
            node_time = numpy.random.normal(n.time, self.deviation_time_rand)
            nodes[i].time = datetime.timedelta(seconds=total_time)
            total_time -= node_time
        nodes.reverse()
        return nodes
        
    def route(self, nodes):
        nodes = self.pre_process_nodes(nodes)
        now = datetime.datetime.now()
        
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
        print(r.json())


        
        
if __name__ == "__main__":
    
    for i in range(5):
        nodes_tucuruvi_santana = [
            UserClient.Node(76, 0),
            UserClient.Node(78, 400),
            UserClient.Node(75, 200),
            UserClient.Node(72, 300),
            UserClient.Node(69, 350),
            UserClient.Node(67, 500),
        ]       
        
        u = UserClient()
        u.register()
        u.route(nodes_tucuruvi_santana)
        # u.unregister()