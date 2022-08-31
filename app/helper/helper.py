from metro_neo4j.metro_neo4j_db import MetroNeo4jDatabase
from metro_sql import sql_helper, schemas, enums


def initialize_stations_table(db):
    stations = MetroNeo4jDatabase().get_stations()
    for i, record in enumerate(stations):
        s = record[0]
        if sql_helper.check_station_registered(db, s.get("name")):
            stations[i] = None
            continue
        lines_record = MetroNeo4jDatabase().get_station_lines(s.get("name"))
        lines = enums.MetroLine.L_INVALID
        for r in lines_record:
            lines |= enums.metro_line_from_value(r.get("b.l"))
        major = s.id if s.id != 0 else 1000
        stations[i] = schemas.StationCreate(
            id=s.id,
            beacon_id_major=major,
            name=s.get("name"),
            subenvironments=0,
            lines=lines
        )
    stations = [s for s in stations if s is not None]
    sql_helper.create_stations(db, stations)
    

def initialize_trains_table(db):
    pass