MATCH (s:Station), (b:Boarding)
WHERE s.name = b.station
CREATE (s)-[:FOOT {time:$$defaulttime$$, station:b.station}]->(b)
CREATE (b)-[:FOOT {time:$$defaulttime$$, station:b.station}]->(s)
