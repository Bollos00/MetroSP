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
        pass
    
    def unregister():
        pass
        
    def route_sacoma_sao_lucas():
        nodes = [110, 112, 115, 118, 120, 242, 245, 243]
        
        
if __name__ == "__main__":
    for i in range(8):
        u = UserClient()
        print(u.id)
        print(u.password)