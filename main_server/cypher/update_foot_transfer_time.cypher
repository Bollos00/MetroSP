MATCH (f:Boarding)-[ft:FOOT]->(t:Boarding)
WHERE f.station = "$$station$$" and t.station = "$$station$$"  
    and f.l = $$fl$$ and f.v = $$fv$$ and t.l = $$tl$$ and t.v = $$tv$$
SET ft.time = $$time$$