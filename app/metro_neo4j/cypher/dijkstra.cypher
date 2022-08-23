MATCH (s:Station {name:'$$start$$'} ), (d:Station{name:'$$destiny$$'})
CALL apoc.algo.dijkstra(
    s,   d,   'FOOT|TRAIN',   'time',   $$defaultweight$$, $$paths$$
)
yield path as path, weight as weight
RETURN path, weight