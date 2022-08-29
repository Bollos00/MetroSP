from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from metro_neo4j.metro_neo4j_db import MetroNeo4jDatabase
from metro_neo4j.cypher.cypher_helper import CypherHelper
from metro_sql import metro_sql_db, models, schemas, sql_helper
import atexit
from fastapi.middleware.cors import CORSMiddleware
from route_planner import route_planner

metro_neo4j = MetroNeo4jDatabase()
metro_sql = metro_sql_db.get_db

models.Base.metadata.create_all(bind=metro_sql_db.engine)
app = FastAPI()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/planner")
def planner(start: str, end: str, options: int = 1):
    return route_planner.route_planner(start, end, options)


@app.post("/create_user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(metro_sql_db.get_db)):
    db_user = sql_helper.get_user(db, user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="UUID already registered")
    return sql_helper.create_user(db, user)

    
@app.post("/create_node", response_model=schemas.Node)
def create_node(node: schemas.NodeCreate, 
                user_password: str,
                db: Session = Depends(metro_sql)):
    auth_result = sql_helper.auth_user(
        db, schemas.UserAuth(id=node.owner_id, password=user_password)
    )
    if not auth_result:
        raise HTTPException(status_code=400, detail="Authentification failed")
    return sql_helper.create_node(db, node)


# Debugging
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)