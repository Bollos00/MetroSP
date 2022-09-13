MATCH (s:Blocking), (b:Boarding)
WHERE s.name = b.station
CREATE (b)-[:EXIT {time:$$defaulttime$$}]->(s)
