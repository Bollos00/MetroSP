MATCH (b0:Boarding), (b1:Boarding)
WHERE b0.station = b1.station AND b0 <> b1
CREATE (b0)-[:FOOT {time:$$defaulttime$$}]->(b1)
