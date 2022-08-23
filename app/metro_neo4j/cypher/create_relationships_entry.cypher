MATCH (s:Blocking), (b:Boarding)
WHERE s.name = b.station
CREATE (s)-[:WALK {time:$$defaulttime$$, station:b.station}]->(b)
