MATCH (f:Boarding)-[ft:WALK]->(t:Boarding)
WHERE f.station = "$$station$$" and t.station = "$$station$$"  
    and f.l = $$fl$$ and f.v = $$fv$$ and t.l = $$tl$$ and t.v = $$tv$$
SET ft.time = $$time$$