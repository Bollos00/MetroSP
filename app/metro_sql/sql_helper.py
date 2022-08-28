from sqlalchemy.orm import Session
import uuid

from . import models, schemas

def add_commit_refresh(db: Session, db_item):
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_user(db: Session, user_id: uuid.UUID):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(id=user.id, password=user.password)
    return add_commit_refresh(db, db_user)


def auth_user(db: Session, user: schemas.UserAuth):
    query_result = db.query(models.User).filter(models.User.id == user.id).one_or_none()
    if query_result is None:
        return False
    return query_result.password == user.password


def create_node(db: Session, node: schemas.NodeCreate):
    db_node = models.Node(node_id=node.node_id, date_time=node.date_time, owner_id=node.owner_id)
    return add_commit_refresh(db, db_node)