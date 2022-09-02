import string
import secrets
import uuid
import requests

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
        payload = {
            'id': str(self.id),
            'password': self.password
        }
        
        r = requests.post(url, json=payload)
        print(r.text)
    
    def unregister(self):
        url = ADDRES + "/delete_user"
        payload = {
            'id': str(self.id),
            'password': self.password
        }
        
        r = requests.post(url, json=payload)
        print(r.text)
        
    def route_sacoma_sao_lucas(self):
        nodes = [110, 112, 115, 118, 120, 242, 245, 243]
        
        
if __name__ == "__main__":
    for i in range(1):
        u = UserClient()
        u.register()
        u.unregister()