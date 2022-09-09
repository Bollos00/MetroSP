from metro_neo4j.metro_neo4j_db import MetroNeo4jDatabase
from metro_sql import sql_helper, schemas

def get_graph():
    return


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