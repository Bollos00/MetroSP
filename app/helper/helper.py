from sqlite3 import dbapi2
from metro_neo4j.metro_neo4j_db import MetroNeo4jDatabase
from metro_sql import sql_helper, schemas, enums, models

def initialize_stations_table(neo4jdb, sqldb):
    sql_helper.clear_stations_table(sqldb)
    stations = MetroNeo4jDatabase().get_stations(neo4jdb)
    for i, record in enumerate(stations):
        s = record[0]
        lines = MetroNeo4jDatabase().get_station_lines(neo4jdb, s.get("name"))
        major = s.id
        subenvs = sqldb.query(models.IndoorNavStationSubenvironment).filter(
            models.IndoorNavStationSubenvironment.station_id == s.id
        )
        subenvs = [a.subenvironment for a in subenvs]
        stations[i] = models.Station(
            id=s.id,
            beacon_id_major=major,
            name=s.get("name"),
            subenvironments=subenvs,
            lines=lines
        )
    sql_helper.create_stations(sqldb, stations)
    

def initialize_trains_table(sqldb):
    sql_helper.clear_trains_table(sqldb)
    trains = list()
    for fleet in enums.MetroFleet:
        train = models.Train(fleet=fleet, lines=[], cars=0, doors=0)
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
            
    