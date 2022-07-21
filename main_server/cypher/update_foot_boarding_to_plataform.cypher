MATCH (f:Boarding)-[ft:WALK]->(t:Station)
WHERE f.station = "$$station$$" and t.name = "$$station$$" and
      f.l = $$fl$$ and f.v = $$fv$$
SET ft.time = $$time$$