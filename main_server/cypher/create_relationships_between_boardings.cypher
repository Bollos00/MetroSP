MATCH (b0:Boarding), (b1:Boarding)
WHERE b0.station = b1.station AND b0 <> b1 AND b0.l <> b1.l
CREATE (b0)-[f:FOOT {time:$$defaulttime$$, station:b0.station}]->(b1)