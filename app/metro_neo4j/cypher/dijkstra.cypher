MATCH (s:Blocking {name:'$$start$$'} ), (e:Blocking{name:'$$end$$'})
CALL apoc.algo.dijkstra(
    s, e, 'ENTER>|EXIT>|TRANSFER>|RIDE>', 'time', $$defaultweight$$, $$paths_count$$
)
YIELD path AS path, weight AS weight
RETURN path, weight