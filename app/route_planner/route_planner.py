from metro_neo4j.metro_neo4j_db import MetroNeo4jDatabase
from metro_sql import sql_helper, models


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
        
    paths = MetroNeo4jDatabase().dijkstra(
        neo4jdb, start, end, paths_count
    )
    
    if len(paths) != paths_count:
        return None

    response = list()
    for i in range(paths_count):
        path = list()
        for j, n in enumerate(paths[i][0].nodes):
            if j==0:
                path.append({
                    "id": n.id,
                    "time": 0
                })
            else:
                time = paths[i][0].relationships[j-1].get("time", 0)
                path.append({
                    "id": n.id,
                    "time": time
                })
        response.append({"path": path, "time": paths[i][1]})
    
    return response
