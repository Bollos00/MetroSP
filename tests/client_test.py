import string
import secrets
import uuid
import requests
import json
import datetime

ADDRES = "http://127.0.0.1:8000"

def random_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(chars) for i in range(length))

class UserClient:
    def __init__(self):
        self.id = uuid.uuid4()
        self.password = random_password()
        
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
        
        
    def route_sacoma_sao_lucas(self):
        nodes = [110, 112, 115, 118, 120, 242, 245, 243]
        url = ADDRES + "/create_nodes"
        nodes.reverse()
        dates = [datetime.datetime.now() for i in nodes]
        for i, d in enumerate(dates):
            dates[i] = d - datetime.timedelta(minutes=2*i)
            nodes[i] = {
                "node_id": nodes[i],
                "date_time": str(dates[i])
            }
        payload = json.dumps({
            "nodes": nodes,
            "user": {
                'id': str(self.id),
                'password': self.password
            }
        }, indent=2)
        
        r = requests.post(url, data=payload)
        print(r.json())
        
        
    # def route(self, )

        
        
if __name__ == "__main__":
    for i in range(1):
        u = UserClient()
        u.register()
        u.route_sacoma_sao_lucas()
        u.unregister()