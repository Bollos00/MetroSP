MATCH ()-[tr:TRAIN]->()
WHERE tr.l = $$l$$ and tr.v = $$v$$ and tr.n = $$n$$
SET ft.time = $$time$$