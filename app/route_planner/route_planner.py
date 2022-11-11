from metro_neo4j.metro_neo4j_db import MetroNeo4jDatabase
from metro_sql import sql_helper, models
import neo4j
from neo4j import graph

def get_graph(neo4jdb):
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

    return {
        "nodes": nodes,
        "relationships": relationships
    }


def check_path(path: graph.Path):
    for i in range(1, len(path.nodes) - 1):
        node = path.nodes[i]
        if "Blocking" in node.labels:
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
    for record in records:
        path: graph.Path = record[0]
        if not check_path(path):
            continue
        nodes: tuple[graph.Node] = path.nodes
        relationships: tuple[graph.Relationship] = path.relationships
        if len(nodes) != len(relationships) + 1:
            continue
        total_time = record[1]
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
