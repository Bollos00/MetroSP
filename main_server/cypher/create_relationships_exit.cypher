MATCH (s:Blocking), (b:Boarding)
WHERE s.name = b.station
CREATE (b)-[:WALK {time:$$defaulttime$$, station:b.station}]->(s)
