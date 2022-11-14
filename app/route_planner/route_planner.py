from metro_neo4j.metro_neo4j_db import MetroNeo4jDatabase
from metro_sql import sql_helper, models
import neo4j
from neo4j import graph
from itertools import combinations


def initialize_stations_table(neo4jdb, sqldb):
    sql_helper.clear_stations_table(sqldb)
    stations = MetroNeo4jDatabase().get_stations(neo4jdb)
    for i, record in enumerate(stations):
        s = record[0]
        lines = MetroNeo4jDatabase().get_station_lines(neo4jdb, s.get("name"))
        major = s.id
        subenvs = sqldb.query(models.IndoorNavSubenvironment).filter(
            models.IndoorNavSubenvironment.station_id == s.id
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
    

graph_backup = None

def get_graph(neo4jdb):
    global graph_backup
    
    if graph_backup is None:
        nodes = MetroNeo4jDatabase().get_graph_nodes(neo4jdb)
        for i, n in enumerate(nodes):
            node = n[0]
            labels = list(node.labels)
            if "Blocking" in labels:
                nodes[i] = {
                    "type": "Blocking",
                    "id": node.id,
                    "name": node.get("name", "")
                }
            elif "Boarding" in labels:
                nodes[i] = {
                    "type": "Boarding",
                    "id": node.id,
                    "station": node.get("station", ""),
                    "w": node.get("w", ""),
                    "l": node.get("l", ""),
                    "n": node.get("n", ""),
                }

        relationships = MetroNeo4jDatabase().get_graph_relationships(neo4jdb)
        for i, r in enumerate(relationships):
            relationship = r[0]
            relationships[i] = {
                "type": relationship.type,
                "id": relationship.id,
                "start": relationship.start_node.id,
                "end": relationship.end_node.id
            }
        graph_backup = {
            "nodes": nodes,
            "relationships": relationships
        }
    return graph_backup


def check_path(path: graph.Path):
    for i in range(1, len(path.nodes) - 1):
        if "Blocking" in path.nodes[i].labels:
            return False

    pairs = [p for p in combinations(path.nodes, 2) if
             p[0].get('station', '0') == p[1].get('station', '1')]
    
    start_station = path.start_node.get('name', '0')
    end_station = path.end_node.get('name', '0')
    
    for p in pairs:
        # Transfer on start or end node!
        p0s = p[0].get('station', '2')
        if p[1].get('station') == p0s and p0s in [start_station, end_station]:
            return False
        # # Boarding of equal linenumbers but opposite ways in path!
        # if p[0].get('l') == p[1].get('l') and p[0].get('n') == p[1].get('n'):
        #     return False
        rls = [rl for rl in path.relationships if
               p[0] in rl.nodes and p[1] in rl.nodes]
        # No direct relationship of transfer
        if not rls:
            return False

    return True
    

def route_planner(neo4jdb, start, end, paths_count):
    try:
        start = int(start)
    except:
        start = MetroNeo4jDatabase().get_station_id(neo4jdb, start)
    try:
        end = int(end)
    except:
        end = MetroNeo4jDatabase().get_station_id(neo4jdb, end)
    
    if start is None or end is None:
        return None
        
    records: list[neo4j.Record] = MetroNeo4jDatabase().dijkstra(
        neo4jdb, start, end, paths_count
    )
    
    if records is None or len(records) == 0:
        return []

    response = list()
    best_time = 9999999
    for record in records:
        path: graph.Path = record[0]
        if not check_path(path):
            continue
        nodes: tuple[graph.Node] = path.nodes
        relationships: tuple[graph.Relationship] = path.relationships
        if len(nodes) != len(relationships) + 1:
            continue
        total_time = record[1]
        if total_time < best_time:
            best_time = total_time
        elif total_time > best_time*1.2:
            continue
        path_json = []
        for j, n in enumerate(nodes):
            path_json.append({
                "node": {
                    "id": n.id
                }
            })
            if j != len(nodes) - 1:
                rl = relationships[j]
                path_json.append({
                    "relationship": {
                        "id": rl.id,
                        "time": rl.get("time")
                    }
                })

        response.append({"path": path_json, "time": total_time})
    
    return response
