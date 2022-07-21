MATCH (f:Station)-[ft:WALK]->(t:Boarding)
WHERE f.name = "$$station$$" and t.station = "$$station$$" and
      t.l = $$tl$$ and t.v = $$tv$$
SET ft.time = $$time$$