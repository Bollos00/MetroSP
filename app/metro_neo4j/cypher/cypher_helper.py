import os

class CypherHelper:
    def __init__(self, t_train_trip=150, t_boarding=10, t_wait_train=300, v_ped=1.0, d_diloc=100):
        abs_dir_path = os.path.dirname(os.path.abspath(__file__))
        with open(f'{abs_dir_path}/create_nodes.cypher', 'r') as f:
            self.create_nodes = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_boarding_names.cypher', 'r') as f:
            self.create_bd_names = CypherHelper.cypher_optimized(f.read())
        
        with open(f'{abs_dir_path}/create_relationships_entry.cypher', 'r') as f:
            self.create_rl_entry = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_relationships_exit.cypher', 'r') as f:
            self.create_rl_exit = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_relationships_train_way_minus.cypher', 'r') as f:
            self.create_rl_train_way_minus = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_relationships_train_way_plus.cypher', 'r') as f:
            self.create_rl_train_way_plus = CypherHelper.cypher_optimized(f.read())
        with open(f'{abs_dir_path}/create_relationships_transfer.cypher', 'r') as f:
            self.create_rl_transfer = CypherHelper.cypher_optimized(f.read())
        
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
    
        t_disloc_train  = int(t_train_trip + t_boarding)
        t_disloc_transf = int(v_ped*d_diloc + t_wait_train/2 + t_boarding)
        t_disloc_exit   = int(v_ped*d_diloc)
        t_disloc_entry  = int(v_ped*d_diloc + t_wait_train/2 + t_boarding)

        self.create_rl_entry = self.create_rl_entry.replace(
            "$$defaulttime$$", str(t_disloc_entry)
        )
        self.create_rl_exit = self.create_rl_exit.replace(
            "$$defaulttime$$", str(t_disloc_exit)
        )
        self.create_rl_train_way_minus = self.create_rl_train_way_minus.replace(
            "$$defaulttime$$", str(t_disloc_train)
        )
        self.create_rl_train_way_plus = self.create_rl_train_way_plus.replace(
            "$$defaulttime$$", str(t_disloc_train)
        )
        self.create_rl_transfer = self.create_rl_transfer.replace(
            "$$defaulttime$$", str(t_disloc_transf)
        )

    @staticmethod
    def cypher_optimized(cypher_code):
        return cypher_code
    
    def get_dijkstra(self, start, end, paths_count, default_weight):
        return self.dijkstra.replace(
            "$$start$$", start
        ).replace(
            "$$end$$", end
        ).replace(
            "$$defaultweight$$", str(default_weight)
        ).replace(
            "$$paths_count$$", str(paths_count)
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