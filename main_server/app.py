from fastapi import FastAPI
from metro_database.metrodatabasedriver import MetroDatabaseDriver
import atexit
from fastapi.middleware.cors import CORSMiddleware
from credentials import credentials

def init_driver():
    uri = credentials.NEO4J_URI
    user = credentials.NEO4J_USER
    password = credentials.NEO4J_PASSWORD

    return MetroDatabaseDriver(uri, user, password)

metro_db = init_driver()    

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}