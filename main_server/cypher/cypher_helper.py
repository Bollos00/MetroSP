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
        with open(f'{abs_dir_path}/update_foot_transfer_time.cypher', 'r') as f:
            self.update_ft_transf = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/update_train_time.cypher', 'r') as f:
            self.update_tr = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/update_foot_boarding_to_plataform.cypher', 'r') as f:
            self.update_ft_bd_plat = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/update_foot_plataform_to_boarding.cypher', 'r') as f:
            self.update_ft_plat_bd = CypherHelper.cypher_optimized(f.read())
    

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
    
    def get_update_tr_time(self, l, v, n, time):
        return self.update_tr.replace(
            "$$l$$", str(l)
        ).replace(
            "$$v$$", str(v)
        ).replace(
            "$$n$$", str(n)
        ).replace(
            "$$time$$", str(int(time))
        )

    def get_update_ft_transf_time(self, station, fl, fv, tl, tv, time):
        return self.update_ft_transf.replace(
            "$$station$$", str(station)
        ).replace(
            "$$fl$$", str(fl)
        ).replace(
            "$$fv$$", str(fv)
        ).replace(
            "$$tl$$", str(tl)
        ).replace(
            "$$tv$$", str(tv)
        ).replace(
            "$$time$$", str(int(time))
        )

    def get_update_ft_bd_plat_time(self, station, fl, fv, time):
        return self.update_ft_bd_plat.replace(
            "$$station$$", str(station)
        ).replace(
            "$$fl$$", str(fl)
        ).replace(
            "$$fv$$", str(fv)
        ).replace(
            "$$time$$", str(int(time))
        )

    def get_update_ft_plat_bd_time(self, station, tl, tv, time):
        return self.update_ft_plat_bd.replace(
            "$$station$$", str(station)
        ).replace(
            "$$tl$$", str(tl)
        ).replace(
            "$$tv$$", str(tv)
        ).replace(
            "$$time$$", str(int(time))
        )

    
if __name__ == "__main__":
    ch = CypherHelper()