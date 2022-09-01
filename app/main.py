from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from metro_neo4j.metro_neo4j_db import MetroNeo4jDatabase
from metro_neo4j.cypher.cypher_helper import CypherHelper
from metro_sql import metro_sql_db, models, schemas, sql_helper
import atexit
from fastapi.middleware.cors import CORSMiddleware
from route_planner import route_planner
from fastapi_utils.tasks import repeat_every
from helper import helper

metro_neo4j = MetroNeo4jDatabase()
metro_sql = metro_sql_db.get_db

models.Base.metadata.create_all(bind=metro_sql_db.engine)
app = FastAPI()


@app.on_event("startup")
def startup_event():
    db = metro_sql_db.SessionLocal()
    helper.initialize_stations_table(db)
    helper.initialize_trains_table(db)
    db.close()


@app.on_event("shutdown")
def shutdown_event():
    pass

@app.on_event("startup")
@repeat_every(seconds=30*60) # 30 minutes
def periodic_db_updates():
    db = metro_sql_db.SessionLocal()
    route_planner.update_node_links_table(db)
    db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/planner")
def planner(start: str, end: str, options: int = 1):
    return route_planner.route_planner(start, end, options)


@app.post("/create_user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(metro_sql)):
    db_user = sql_helper.get_user(db, user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="UUID already registered")
    return sql_helper.create_user(db, user)


@app.post("/delete_user")
def delete_user(user: schemas.UserAuth, db: Session = Depends(metro_sql)):
    auth_result = sql_helper.auth_user(db, user)
    if not auth_result:
        raise HTTPException(status_code=400, detail="Authentification failed")
    sql_helper.delete_user(db, user)

    
@app.post("/create_nodes")
def create_nodes(nodes: list[schemas.NodeCreate], 
                 user: schemas.UserAuth,
                 db: Session = Depends(metro_sql)):
    auth_result = sql_helper.auth_user(db, user)
    if not auth_result:
        raise HTTPException(status_code=400, detail="Authentification failed")
    sql_helper.create_nodes(db, nodes, user.id)


@app.get("/test")
def test(db: Session = Depends(metro_sql)):
    return route_planner.update_node_links_table(db)


# Debugging
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)