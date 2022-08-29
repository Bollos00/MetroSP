from metro_neo4j.metro_neo4j_db import MetroNeo4jDatabase

def route_planner(start, end, paths_count):
    db = MetroNeo4jDatabase()
    paths = db.dijkstra(start, end, paths_count)
    if len(paths) != paths_count:
        return None

    response = list()
    for i in range(paths_count):
        path = list()
        for j, n in enumerate(paths[i][0].nodes):
            if j==0:
                path.append((n.get("name", ""), 0))
            else:
                time = paths[i][0].relationships[j-1].get("time", 0)
                path.append((n.get("name", ""), time))
        response.append({"path": path, "time": paths[i][1]})
    
    return response