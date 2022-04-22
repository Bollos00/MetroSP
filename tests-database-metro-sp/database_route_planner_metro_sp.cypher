// Cria estações
CREATE
    (saude:Station {name:"Saúde"}),
    (L01_N20_V1:Boarding {station:"Saúde", l:1, n:20, v:1}),
    (L01_N20_V2:Boarding {station:"Saúde", l:1, n:20, v:2}),
    
    (praca_da_arvore:Station {name:"Praça da árvore"}),
    (L01_N19_V1:Boarding {station:"Praça da árvore", l:1, n:19, v:1}),
    (L01_N19_V2:Boarding {station:"Praça da árvore", l:1, n:19, v:2}),

    (santa_cruz:Station {name:"Santa Cruz"}),
    (L01_N18_V1:Boarding {station:"Santa Cruz", l:1, n:18, v:1}),
    (L01_N18_V2:Boarding {station:"Santa Cruz", l:1, n:18, v:2}),
    (L05_N18_V1:Boarding {station:"Santa Cruz", l:5, n:15, v:1}),
    (L05_N18_V2:Boarding {station:"Santa Cruz", l:5, n:15, v:2}),


    (vila_mariana:Station {name:"Vila Mariana"}),
    (L01_N17_V1:Boarding {station:"Vila Mariana", l:1, n:17, v:1}),
    (L01_N17_V2:Boarding {station:"Vila Mariana", l:1, n:17, v:2}),

    (ana_rosa:Station {name:"Ana Rosa"}),
    (L01_N16_V1:Boarding {station:"Ana Rosa", l:1, n:16, v:1}),
    (L01_N16_V2:Boarding {station:"Ana Rosa", l:1, n:16, v:2}),
    (L02_N08_V1:Boarding {station:"Ana Rosa", l:2, n:8,  v:1}),
    (L02_N08_V2:Boarding {station:"Ana Rosa", l:2, n:8,  v:2}),

    (paraiso:Station {name:"Paraíso"}),
    (L01_N15_V1:Boarding {station:"Paraíso", l:1, n:15, v:1}),
    (L01_N15_V2:Boarding {station:"Paraíso", l:1, n:15, v:2}),
    (L02_N07_V1:Boarding {station:"Paraíso", l:2, n:7,  v:1}),
    (L02_N07_V2:Boarding {station:"Paraíso", l:2, n:7,  v:2}),

    (vergueiro:Station {name:"Vergueiro"}),
    (L01_N14_V1:Boarding {station:"Vergueiro", l:1, n:14, v:1}),
    (L01_N14_V2:Boarding {station:"Vergueiro", l:1, n:14, v:2}),

    (sao_joaquim:Station {name:"São Joaquim"}),
    (L01_N13_V1:Boarding {station:"São Joaquim", l:1, n:13, v:1}),
    (L01_N13_V2:Boarding {station:"São Joaquim", l:1, n:13, v:2})


// Cria ligações
MATCH (s:Station), (b:Boarding)
WHERE s.name = b.station
CREATE (s)-[:FOOT {time:120}]->(b)
CREATE (b)-[:FOOT {time:120}]->(s)

MATCH (b0:Boarding), (b1:Boarding)
WHERE b0.station = b1.station AND b0 <> b1
CREATE (b0)-[:FOOT {time:120}]->(b1)

// Via 1
MATCH (b0:Boarding), (b1:Boarding)
WHERE b0.l = b1.l AND b0.v = 1 and b1.v = 1 and (b0.n - b1.n = 1)
CREATE (b0)-[:TRAIN {time:120}]->(b1)

// Via 2
MATCH (b0:Boarding), (b1:Boarding)
WHERE b0.l = b1.l AND b0.v = 2 and b1.v = 2 and (b1.n - b0.n = 1)
CREATE (b0)-[:TRAIN {time:120}]->(b1)


// Chamando o planejador de rotas
// MATCH (start:Station {name: 'São Joaquim'}), (end:Station {name: 'Saúde'})
// CALL apoc.algo.dijkstra(start, end, null, 'time', 200, 1) YIELD path, weight
// RETURN path, weight