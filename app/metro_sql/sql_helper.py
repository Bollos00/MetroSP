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


def delete_nodes(db:Session, nodes: list[models.Node]):
    for n in nodes:
        db.delete(n)
    db.commit()

def create_node_link(db: Session, node_link: schemas.NodeLinkCreate):
    disp_time = (node_link.end_date_time - node_link.start_date_time).total_seconds()

    db_node_link = models.NodeLink(
        node_link_id=node_link.node_link_id, 
        start_date_time=node_link.start_date_time,
        end_date_time=node_link.end_date_time,
        displacement_time_s=disp_time
    )
    return add_commit_refresh(db, db_node_link)

def get_users_with_nodes(db: Session):
    users = db.query(models.Node.owner_id).distinct()
    users = [u.owner_id for u in users]
    nodes = dict()
    for u in users:
        user_nodes = db.query(models.Node).filter(
            models.Node.owner_id == u
        ).all()
        nodes[u] = sorted(user_nodes, key=lambda n: n.date_time)
    return nodes
