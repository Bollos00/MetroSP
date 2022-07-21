MATCH (b0:Boarding), (b1:Boarding)
WHERE b0.l = b1.l AND b0.w = '+' and b1.w = '+' and (b1.n - b0.n = 1)
CREATE (b0)-[:RIDE {time:$$defaulttime$$}]->(b1)
