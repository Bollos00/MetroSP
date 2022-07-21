MATCH ()-[tr:RIDE]->()
WHERE tr.l = $$l$$ and tr.v = $$v$$ and tr.n = $$n$$
SET tr.time = $$time$$