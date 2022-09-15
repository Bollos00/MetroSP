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
import uuid

metro_sql = metro_sql_db.get_session
metro_neo4j = MetroNeo4jDatabase.get_session

models.Base.metadata.create_all(bind=metro_sql_db.engine)
app = FastAPI()

@app.on_event("startup")
def startup_event():
    MetroNeo4jDatabase().reset()
    
    sqldb = metro_sql_db.SessionLocal()
    neo4jdb = MetroNeo4jDatabase().driver.session()
    
    helper.initialize_stations_table(neo4jdb, sqldb)
    helper.initialize_trains_table(sqldb)
    sql_helper.initialize_valid_uuids_table(sqldb)
    
    sqldb.close()
    neo4jdb.close()


@app.on_event("shutdown")
def shutdown_event():
    pass


@app.on_event("startup")
@repeat_every(seconds=1*60) # 1 minute
def periodic_db_updates():
    sqldb = metro_sql_db.SessionLocal()
    route_planner.update_node_links_table(sqldb)
    sqldb.close()


@app.on_event("startup")
@repeat_every(seconds=4*60) # 4 minutes
def periodic_db_updates():
    sqldb = metro_sql_db.SessionLocal()
    neo4jdb = MetroNeo4jDatabase().driver.session()
    route_planner.update_node_links_graph(neo4jdb, sqldb)
    sqldb.close()
    neo4jdb.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/planner")
def planner(start: str, end: str, options: int = 1, neo4jdb = Depends(metro_neo4j)):
    return route_planner.route_planner(neo4jdb, start, end, options)


@app.get("/get_planner_graph")
def planner_graph(neo4jdb = Depends(metro_neo4j)):
    return route_planner.get_graph(neo4jdb)


@app.post("/create_user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, sqldb: Session = Depends(metro_sql)):
    db_user = sql_helper.get_user(sqldb, user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="UUID already registered")
    return sql_helper.create_user(sqldb, user)


@app.post("/delete_user")
def delete_user(user: schemas.UserAuth, sqldb: Session = Depends(metro_sql)):
    auth_result = sql_helper.auth_user(sqldb, user)
    if not auth_result:
        raise HTTPException(status_code=400, detail="Authentification failed")
    sql_helper.delete_user(sqldb, user.id)

    
@app.post("/create_nodes")
def create_nodes(nodes: list[schemas.NodeCreate], 
                 user: schemas.UserAuth,
                 sqldb: Session = Depends(metro_sql)):
    auth_result = sql_helper.auth_user(sqldb, user)
    if not auth_result:
        raise HTTPException(status_code=400, detail="Authentification failed")
    sql_helper.create_nodes(sqldb, nodes, user.id)


@app.get("/valid_uuids", response_model=list[uuid.UUID])
def valid_uuids(sqldb: Session = Depends(metro_sql)):
    return sql_helper.get_valid_uuids(sqldb)

@app.get("/test")
def test(db: Session = Depends(metro_sql)):
    return route_planner.update_node_links_table(db)


# Debugging
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)