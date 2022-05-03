MATCH (f:Station)-[ft:FOOT]->(t:Boarding)
WHERE f.name = "$$station$$" and t.station = "$$station$$" and
      t.l = $$tl$$ and t.v = $$tv$$
SET ft.time = $$time$$