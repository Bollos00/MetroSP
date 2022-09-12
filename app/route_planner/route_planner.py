from metro_neo4j.metro_neo4j_db import MetroNeo4jDatabase
from metro_sql import sql_helper, schemas

def get_graph():
    nodes = MetroNeo4jDatabase().get_graph_nodes()
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

    relationships = MetroNeo4jDatabase().get_graph_relationships()
    for i, r in enumerate(relationships):
        relationship = r[0]
        relationships[i] = {
            "type": relationship.type,
            "start": relationship.start_node.id,
            "end": relationship.end_node.id
        }

    return {
        "nodes": nodes,
        "relationships": relationships
    }


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


def update_node_links_table(db):
    nodes = sql_helper.get_users_with_nodes(db)
    nodes_to_delete = list()
    for u in nodes.keys():
        user_nodes = nodes[u]
        for i in range(len(user_nodes)-1):
            start_node = user_nodes[i]
            nodes_to_delete.append(start_node)
            end_node = user_nodes[i+1]
            rl = MetroNeo4jDatabase().get_relationship_id_from_nodes_ids(
                start_node.node_id, end_node.node_id
            )
            if len(rl) != 1:
                continue
            rl_id = rl[0][0].id
            sql_helper.create_node_link(
                db,
                schemas.NodeLinkCreate(
                    node_link_id=rl_id,
                    start_date_time=start_node.date_time,
                    end_date_time=end_node.date_time,
                )
            )
    sql_helper.delete_nodes(db, nodes_to_delete)
    
    
def update_node_links_graph(db):
    pass