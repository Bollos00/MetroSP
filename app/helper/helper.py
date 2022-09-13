from metro_neo4j.metro_neo4j_db import MetroNeo4jDatabase
from metro_sql import sql_helper, schemas, enums, models


def initialize_stations_table(neo4jdb, sqldb):
    stations = MetroNeo4jDatabase().get_stations(neo4jdb)
    for i, record in enumerate(stations):
        s = record[0]
        if sql_helper.check_station_registered(sqldb, s.get("name")):
            stations[i] = None
            continue
        lines_record = MetroNeo4jDatabase().get_station_lines(neo4jdb, s.get("name"))
        lines = enums.MetroLine.L_INVALID
        for r in lines_record:
            lines |= enums.metro_line_from_value(r.get("b.l"))
        major = s.id
        stations[i] = schemas.StationCreate(
            id=s.id,
            beacon_id_major=major,
            name=s.get("name"),
            subenvironments=0,
            lines=lines
        )
    stations = [s for s in stations if s is not None]
    sql_helper.create_stations(sqldb, stations)
    

def initialize_trains_table(sqldb):
    trains = list()
    for fleet in enums.MetroFleet:
        if sql_helper.check_train_registered(sqldb, fleet):
            continue
        train = models.Train(fleet=fleet, cars=0, doors=0)
        if fleet == enums.MetroFleet.FLEET_E:
            train.beacon_id_major_begin = 1001 
            train.beacon_id_major_end   = 2000
        elif fleet == enums.MetroFleet.FLEET_G:
            train.beacon_id_major_begin = 3001 
            train.beacon_id_major_end   = 4000
        elif fleet == enums.MetroFleet.FLEET_H:
            train.beacon_id_major_begin = 5001 
            train.beacon_id_major_end   = 6000
        elif fleet == enums.MetroFleet.FLEET_I:
            train.beacon_id_major_begin = 7001 
            train.beacon_id_major_end   = 8000
        elif fleet == enums.MetroFleet.FLEET_J:
            train.beacon_id_major_begin = 9001 
            train.beacon_id_major_end   = 10000
        elif fleet == enums.MetroFleet.FLEET_K:
            train.beacon_id_major_begin = 11001 
            train.beacon_id_major_end   = 12000
        elif fleet == enums.MetroFleet.FLEET_L:
            train.beacon_id_major_begin = 13001 
            train.beacon_id_major_end   = 14000
        elif fleet == enums.MetroFleet.FLEET_M:
            train.beacon_id_major_begin = 15001 
            train.beacon_id_major_end   = 16000
        trains.append(train)
    sql_helper.create_trains(sqldb, trains)
            
    