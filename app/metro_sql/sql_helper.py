import datetime
from sqlalchemy.orm import Session
import uuid

from . import models, schemas, enums
from indoor_nav import indoor_nav


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
    if user is None:
        return
    
    user_nodes = db.query(models.Node).filter(
        models.Node.owner_id == user_id
    ).all()
    delete_nodes(db, user_nodes)
    db.delete(user)
    db.commit()
    
    return {"result": "ok"}


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
    
    return {"result": "ok"}


def delete_nodes(db:Session, nodes: list[models.Node]):
    for n in nodes:
        db.delete(n)
    db.commit()


def create_node_links(db: Session, node_links: list[models.NodeLink]):
    for nl in node_links:
        db.add(nl)
    db.commit()


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


def get_users_with_node_links(db: Session, limit_time: datetime.timedelta):
    then = datetime.datetime.now() - limit_time
    node_links = db.query(models.NodeLink).filter(
        models.NodeLink.end_date_time > then
    )
    
    node_link_ids = set([n.node_link_id for n in node_links])
    
    elements = dict()
    for nl_id in node_link_ids:
        nl = node_links.filter(models.NodeLink.node_link_id == nl_id)
        nl = [[x.start_date_time.timestamp(), x.displacement_time_s] for x in nl]
        elements[nl_id] = nl
    return elements


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


def clear_trains_table(db: Session):
    db.query(models.Train).delete()
    db.commit()


def clear_stations_table(db: Session):
    db.query(models.Station).delete()
    db.commit()


def create_stations(db: Session, stations: list[models.Station]):
    for s in stations:
        db.add(s)
    db.commit()
    
    
def create_trains(db: Session, trains: list[models.Train]):
    for t in trains:
        db.add(t)
    db.commit()
    

def get_valid_uuids(db: Session):
    uuids = db.query(models.ValidUUID.uuid).distinct().all()
    return [u.uuid for u in uuids]


def initialize_valid_uuids_table(db: Session):
    valid_uuids_db = get_valid_uuids(db)
    uuids = ["bc3411a4-3198-45c0-aefe-3f4985a0400f"]
    uuids = [uuid.UUID(u) for u in uuids]
    for u in uuids:
        if u not in valid_uuids_db:
            db.add(models.ValidUUID(uuid=u))
    db.commit()


def _clear_indoor_nav_tables(db: Session):
    for M in [
        models.IndoorNavBeacon,
        models.IndoorNavPoi,
        models.IndoorNavStationCircleObstacle,
        models.IndoorNavStationPolygonObstacle,
        models.IndoorNavStationSubenvironment,
        models.IndoorNavStationTransition
    ]:
        db.query(M).delete()
    db.commit()


def initialize_indoor_nav_tables(db: Session):
    _clear_indoor_nav_tables(db)
    
    stations_json = indoor_nav.get_stations()
    for station_info in stations_json:
        station_id = station_info["station_id"]
        _add_station_beacons(db, station_id, station_info["beacons"])
        _add_station_circle_obstacles(db, station_id, station_info["circle_obstacles"])
        _add_station_pois(db, station_id, station_info["pois"])
        _add_station_polygon_obstacles(
            db, station_id, station_info["polygon_obstacles"]
        )
        _add_station_subenvironments(db, station_id, station_info["subenvironments"])
        _add_station_transitions(db, station_id, station_info["transitions"])
    db.commit()


def backup_indoor_nav_tables(db: Session):
    station_ids = db.query(models.Station.id).distinct().all()
    station_ids = [s.id for s in station_ids]
    indoor_nav.backup()
    indoor_nav_info = get_indoor_nav_info(db, station_ids)
    for station_info in indoor_nav_info:
        station_id = station_info["station_id"]
        station = db.query(models.Station).filter(
            models.Station.id == station_id
        ).one_or_none()
        if station is None:
            continue
        indoor_nav.save_station(station_info, station.name)

  
def _add_station_subenvironments(db: Session, station_id, subenvs):
    for subenv in subenvs:
        db.add(models.IndoorNavStationSubenvironment(
            station_id = station_id,
            subenvironment = subenv["subenvironment"],
            limit_points = subenv["limit_points"]
        ))


def _add_station_polygon_obstacles(db: Session, station_id, polygons):
    for pol in polygons:
        db.add(models.IndoorNavStationPolygonObstacle(
            station_id = station_id,
            subenvironment = pol["subenvironment"],
            points = pol["points"]
        ))

    
def _add_station_circle_obstacles(db: Session, station_id, circles):
    for circle in circles:
        db.add(models.IndoorNavStationPolygonObstacle(
            station_id = station_id,
            subenvironment = circle["subenvironment"],
            c_x = circle["c_x"],
            c_y = circle["c_y"],
            r = circle["r"],
        ))


def _add_station_transitions(db: Session, station_id, transitions):
    for transition in transitions:
        db.add(models.IndoorNavStationTransition(
            station_id = station_id,
            directional = transition["directional"],
            transition_type = transition["transition_type"],
            subenvironment_start = transition["subenvironment_start"],
            subenvironment_end = transition["subenvironment_end"],
            direction_angle_start = transition["direction_angle_start"],
            start_x = transition["start_x"],
            start_y = transition["start_y"],
            direction_angle_end = transition["direction_angle_end"],
            end_x = transition["end_x"],
            end_y = transition["end_y"],
        ))

    
def _add_station_pois(db: Session, station_id, pois):
    for poi in pois:
        db.add(models.IndoorNavPoi(
            station_id = station_id,
            subenvironment = poi["subenvironment"],
            poi_type = poi["poi_type"],
            line_way = poi["line_way"],
            x = poi["x"],
            y = poi["y"],
        ))
    

def _add_station_beacons(db: Session, station_id, beacons):
    for beacon in beacons:
        db.add(models.IndoorNavBeacon(
            station_id = station_id,
            subenvironment = beacon["subenvironment"],
            beacon_id_minor = beacon["beacon_id_minor"],
            x = beacon["x"],
            y = beacon["y"],
            z = beacon["z"]
        ))

  
def _get_station_subenvironments(db: Session, station_id):
    subenvs = db.query(models.IndoorNavStationSubenvironment).filter(
        models.IndoorNavStationSubenvironment.station_id == station_id
    )
    
    return [{
        'subenvironment': a.subenvironment,
        'limit_points': a.limit_points
    } for a in subenvs]


def _get_station_polygon_obstacles(db: Session, station_id):
    obstacles = db.query(models.IndoorNavStationPolygonObstacle).filter(
        models.IndoorNavStationPolygonObstacle.station_id == station_id
    )
    
    return [{
        'subenvironment': a.subenvironment,
        'points': a.points
    } for a in obstacles]

    
def _get_station_circle_obstacles(db: Session, station_id):
    obstacles = db.query(models.IndoorNavStationCircleObstacle).filter(
        models.IndoorNavStationCircleObstacle.station_id == station_id
    )
    
    return [{
        'subenvironment': a.subenvironment,
        'c_x': a.c_x,
        'c_y': a.c_y,
        'r': a.r
    } for a in obstacles]


def _get_station_transitions(db: Session, station_id):
    transitions = db.query(models.IndoorNavStationTransition).filter(
        models.IndoorNavStationTransition.station_id == station_id
    )
    
    return [{
        'directional': a.directional,
        'transition_type': a.transition_type.name,
        'subenvironment_start': a.subenvironment_start,
        'subenvironment_end': a.subenvironment_end,
        'direction_angle_start': a.direction_angle_start,
        'start_x': a.start_x,
        'start_y': a.start_y,
        'direction_angle_end': a.direction_angle_end,
        'end_x': a.end_x,
        'end_y': a.end_y
    } for a in transitions]

    
def _get_station_pois(db: Session, station_id):
    pois = db.query(models.IndoorNavPoi).filter(
        models.IndoorNavPoi.station_id == station_id
    )
    
    return [{
        'subenvironment': a.subenvironment,
        'poi_type': a.poi_type.name,
        'line_way': a.line_way,
        'x': a.x,
        'y': a.y
    } for a in pois]


def _get_station_beacons(db: Session, station_id):
    beacons = db.query(models.IndoorNavBeacon).filter(
        models.IndoorNavBeacon.station_id == station_id
    )
    
    return [{
        'subenvironment': a.subenvironment,
        'beacon_id_minor': a.beacon_id_minor,
        'x': a.x,
        'y': a.y,
        'z': a.z
    } for a in beacons]

    
def get_indoor_nav_info(db: Session, station_ids: list[int]):
    info = station_ids.copy()
    for i, station_id in enumerate(station_ids):
        station_info = dict()
        station_info['station_id'] = station_id
        station_info['subenvironments'] = _get_station_subenvironments(db, station_id)
        station_info['polygon_obstacles'] = _get_station_polygon_obstacles(db, station_id)
        station_info['circle_obstacles'] = _get_station_circle_obstacles(db, station_id)
        station_info['transitions'] = _get_station_transitions(db, station_id)
        station_info['pois'] = _get_station_pois(db, station_id)
        station_info['beacons'] = _get_station_beacons(db, station_id)
        
        info[i] = station_info
    return info