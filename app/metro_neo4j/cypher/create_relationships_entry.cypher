MATCH (s:Blocking), (b:Boarding)
WHERE s.name = b.station
CREATE (s)-[:ENTER {time:$$defaulttime$$}]->(b)
