// Cria estações
CREATE
    (jabaquara:Station {name:"Jabaquara"}),
    (L01_N23_V1:Boarding {station:"Jabaquara", l:1, n:23, v:1}),
    (L01_N23_V2:Boarding {station:"Jabaquara", l:1, n:23, v:2}),
    
    (conceicao:Station {name:"Conceição"}),
    (L01_N22_V1:Boarding {station:"Conceição", l:1, n:22, v:1}),
    (L01_N22_V2:Boarding {station:"Conceição", l:1, n:22, v:2}),
    
    (sao_judas:Station {name:"São Judas"}),
    (L01_N21_V1:Boarding {station:"São Judas", l:1, n:21, v:1}),
    (L01_N21_V2:Boarding {station:"São Judas", l:1, n:21, v:2}),
    
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
    (L01_N13_V2:Boarding {station:"São Joaquim", l:1, n:13, v:2}),

    (liberdade:Station {name:"Liberdade"}),
    (L01_N12_V1:Boarding {station:"Liberdade", l:1, n:12, v:1}),
    (L01_N12_V2:Boarding {station:"Liberdade", l:1, n:12, v:2}),

    (se:Station {name:"Sé"}),
    (L01_N11_V1:Boarding {station:"Sé", l:1, n:11, v:1}),
    (L01_N11_V2:Boarding {station:"Sé", l:1, n:11, v:2}),
    (L03_N06_V1:Boarding {station:"Sé", l:3, n:6,  v:1}),
    (L03_N06_V2:Boarding {station:"Sé", l:3, n:6,  v:2}),

    (sao_bento:Station {name:"São Bento"}),
    (L01_N10_V1:Boarding {station:"São Bento", l:1, n:10, v:1}),
    (L01_N10_V2:Boarding {station:"São Bento", l:1, n:10, v:2}),

    (luz:Station {name:"Luz"}),
    (L01_N09_V1:Boarding {station:"Luz", l:1, n:9,  v:1}),
    (L01_N09_V2:Boarding {station:"Luz", l:1, n:9,  v:2}),
    (L04_N09_V1:Boarding {station:"Luz", l:4, n:9,  v:1}),
    (L04_N09_V2:Boarding {station:"Luz", l:4, n:9,  v:2}),

    (tiradentes:Station {name:"Tiradentes"}),
    (L01_N08_V1:Boarding {station:"Tiradentes", l:1, n:8,  v:1}),
    (L01_N08_V2:Boarding {station:"Tiradentes", l:1, n:8,  v:2}),

    (armenia:Station {name:"Armênia"}),
    (L01_N07_V1:Boarding {station:"Armênia", l:1, n:7,  v:1}),
    (L01_N07_V2:Boarding {station:"Armênia", l:1, n:7,  v:2}),

    (tiete:Station {name:"Tietê"}),
    (L01_N06_V1:Boarding {station:"Tietê", l:1, n:6,  v:1}),
    (L01_N06_V2:Boarding {station:"Tietê", l:1, n:6,  v:2}),

    (carandiru:Station {name:"Carandiru"}),
    (L01_N05_V1:Boarding {station:"Carandiru", l:1, n:5,  v:1}),
    (L01_N05_V2:Boarding {station:"Carandiru", l:1, n:5,  v:2}),

    (santana:Station {name:"Santana"}),
    (L01_N04_V1:Boarding {station:"Santana", l:1, n:4,  v:1}),
    (L01_N04_V2:Boarding {station:"Santana", l:1, n:4,  v:2}),

    (jardim_sao_paulo:Station {name:"Jardim São Paulo"}),
    (L01_N03_V1:Boarding {station:"Jardim São Paulo", l:1, n:3,  v:1}),
    (L01_N03_V2:Boarding {station:"Jardim São Paulo", l:1, n:3,  v:2}),

    (parada_inglesa:Station {name:"Parada Inglesa"}),
    (L01_N02_V1:Boarding {station:"Parada Inglesa", l:1, n:2,  v:1}),
    (L01_N02_V2:Boarding {station:"Parada Inglesa", l:1, n:2,  v:2}),

    (tucuruvi:Station {name:"Tucuruvi"}),
    (L01_N01_V1:Boarding {station:"Tucuruvi", l:1, n:1,  v:1}),
    (L01_N01_V2:Boarding {station:"Tucuruvi", l:1, n:1,  v:2})

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
MATCH (start:Station {name: 'São Joaquim'}), (end:Station {name: 'Saúde'})
CALL apoc.algo.dijkstra(start, end, null, 'time', 200, 1) YIELD path, weight
RETURN path, weight