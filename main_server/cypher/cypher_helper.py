import os

class CypherHelper:
    def __init__(self, default_travel_time = 120):
        abs_dir_path = os.path.dirname(os.path.abspath(__file__))
        with open(f'{abs_dir_path}/create_nodes.cypher', 'r') as f:
            self.create_nodes = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_relationships_between_boardings.cypher', 'r') as f:
            self.create_rl_board = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_relationships_between_stations.cypher', 'r') as f:
            self.create_rl_station = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_relationships_via1.cypher', 'r') as f:
            self.create_rl_v1 = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_relationships_via2.cypher', 'r') as f:
            self.create_rl_v2 = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/dijkstra.cypher', 'r') as f:
            self.dijkstra = CypherHelper.cypher_optimized(f.read())

        self.create_rl_board = self.create_rl_board.replace(
            "$$defaulttime$$", str(default_travel_time)
        )
        self.create_rl_station = self.create_rl_station.replace(
            "$$defaulttime$$", str(default_travel_time)
        )
        self.create_rl_v1 = self.create_rl_v1.replace(
            "$$defaulttime$$", str(default_travel_time)
        )
        self.create_rl_v2 = self.create_rl_v2.replace(
            "$$defaulttime$$", str(default_travel_time)
        )   

    @staticmethod
    def cypher_optimized(cypher_code):
        return cypher_code
    
    def get_dijkstra(self, start, destiny, default_weight, paths):
        # return self.dijkstra.translate({
        #     "$$start$$": start,
        #     "$$destiny$$": destiny,
        #     "$$defaultweight$$": str(default_weight),
        #     "$$paths$$": str(paths)
        # })
        return self.dijkstra.replace(
            "$$start$$", start
        ).replace(
            "$$destiny$$", destiny
        ).replace(
            "$$defaultweight$$", str(default_weight)
        ).replace(
            "$$paths$$", str(paths)
        ).replace(
            "$$start$$", start
        )
    
if __name__ == "__main__":
    ch = CypherHelper()