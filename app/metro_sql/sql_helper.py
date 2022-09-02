from sqlalchemy.orm import Session
import uuid

from . import models, schemas, enums


def add_commit_refresh(db: Session, db_item):
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_user(db: Session, user_id: uuid.UUID):
    return db.query(models.User).filter(models.User.id == user_id).one_or_none()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(id=user.id, password=user.password)
    return add_commit_refresh(db, db_user)


def delete_user(db: Session, user_id: uuid.UUID):
    user = get_user(db, user_id)
    if user is not None:
        db.delete(user)
    db.commit()


def auth_user(db: Session, user: schemas.UserAuth):
    db_user = get_user(db, user.id)
    if db_user is None:
        return False
    return db_user.password == user.password


def create_nodes(db: Session, nodes: list[schemas.NodeCreate], user_id: uuid.UUID):
    for n in nodes:
        db_node = models.Node(
            node_id=n.node_id, date_time=n.date_time, owner_id=user_id
        )
        db.add(db_node)
    db.commit()


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


def check_station_registered(db: Session, station_name: str):
    station_qr = db.query(models.Station).filter(
        models.Station.name == station_name
    ).one_or_none()
    return station_qr is not None


def check_train_registered(db: Session, fleet: enums.MetroFleet):
    fleet_qr = db.query(models.Train).filter(
        models.Train.fleet == fleet
    ).one_or_none()
    return fleet_qr is not None


def create_stations(db: Session, stations: list[schemas.StationCreate]):
    for s in stations:
        db_s = models.Station(
            id = s.id,
            beacon_id_major = s.beacon_id_major,
            name = s.name,
            subenvironments = s.subenvironments,
            lines = s.lines
        )
        db.add(db_s)
    db.commit()
    
    
def create_trains(db: Session, trains: list[models.Train]):
    for t in trains:
        db.add(t)
    db.commit()