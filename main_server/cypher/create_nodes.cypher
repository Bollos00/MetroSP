// Cria estações
CREATE
    // Linha azul (L1) e transferências
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
    (L04_N09_V1:Boarding {station:"Luz", l:4, n:11,  v:1}),
    (L04_N09_V2:Boarding {station:"Luz", l:4, n:11,  v:2}),

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
    (L01_N01_V2:Boarding {station:"Tucuruvi", l:1, n:1,  v:2}),

    // Linha verde (L2)
    (vila_madalena:Station {name:"Vila Madalena"}),
    (L02_N01_V1:Boarding {station:"Vila Madalena", l:2, n:1,  v:1}),
    (L02_N01_V2:Boarding {station:"Vila Madalena", l:2, n:1,  v:2}),

    (:Station {name:"Sumaré"}),
    (:Boarding {station:"Sumaré", l:2, n:2,  v:1}),
    (:Boarding {station:"Sumaré", l:2, n:2,  v:2}),

    (:Station  {name:   "Clínicas"}),
    (:Boarding {station:"Clínicas", l:2, n:3,  v:1}),
    (:Boarding {station:"Clínicas", l:2, n:3,  v:2}),

    (:Station  {name:   "Paulista"}),
    (:Boarding {station:"Paulista", l:2, n:4,  v:1}),
    (:Boarding {station:"Paulista", l:2, n:4,  v:2}),
    (:Boarding {station:"Paulista", l:4, n:8,  v:1}),
    (:Boarding {station:"Paulista", l:4, n:8,  v:2}),

    (:Station  {name:   "Trianon"}),
    (:Boarding {station:"Trianon", l:2, n:5,  v:1}),
    (:Boarding {station:"Trianon", l:2, n:5,  v:2}),

    (:Station  {name:   "Brigadeiro"}),
    (:Boarding {station:"Brigadeiro", l:2, n:6,  v:1}),
    (:Boarding {station:"Brigadeiro", l:2, n:6,  v:2}),

    // Ana Rosa (já definido)
    // Paraíso  (já definido)

    (:Station  {name:   "Chácara Klabin"}),
    (:Boarding {station:"Chácara Klabin", l:2, n:9,  v:1}),
    (:Boarding {station:"Chácara Klabin", l:2, n:9,  v:2}),
    (:Boarding {station:"Chácara Klabin", l:5, n:16,  v:1}),
    (:Boarding {station:"Chácara Klabin", l:5, n:16,  v:2}),

    (:Station  {name:   "Santos Imigrantes"}),
    (:Boarding {station:"Santos Imigrantes", l:2, n:10,  v:1}),
    (:Boarding {station:"Santos Imigrantes", l:2, n:10,  v:2}),

    (:Station  {name:   "Alto do Ipiranga"}),
    (:Boarding {station:"Alto do Ipiranga", l:2, n:11,  v:1}),
    (:Boarding {station:"Alto do Ipiranga", l:2, n:11,  v:2}),

    (:Station  {name:   "Sacomã"}),
    (:Boarding {station:"Sacomã", l:2, n:12,  v:1}),
    (:Boarding {station:"Sacomã", l:2, n:12,  v:2}),

    (:Station  {name:   "Tamanduateí"}),
    (:Boarding {station:"Tamanduateí", l:2, n:13,  v:1}),
    (:Boarding {station:"Tamanduateí", l:2, n:13,  v:2}),

    (:Station  {name:   "Vila Prudente"}),
    (:Boarding {station:"Vila Prudente", l:2, n:14,  v:1}),
    (:Boarding {station:"Vila Prudente", l:2, n:14,  v:2}),
    (:Boarding {station:"Vila Prudente", l:15, n:1,  v:1}),
    (:Boarding {station:"Vila Prudente", l:15, n:1,  v:2}),

    // Linha vermelha (L3)
    (:Station  {name:   "Barra Funda"}),
    (:Boarding {station:"Barra Funda", l:3, n:1,  v:1}),
    (:Boarding {station:"Barra Funda", l:3, n:1,  v:2}),

    (:Station  {name:   "Mal. Deodoro"}),
    (:Boarding {station:"Mal. Deodoro", l:3, n:2,  v:1}),
    (:Boarding {station:"Mal. Deodoro", l:3, n:2,  v:2}),

    (:Station  {name:   "Santa Cecília"}),
    (:Boarding {station:"Santa Cecília", l:3, n:3,  v:1}),
    (:Boarding {station:"Santa Cecília", l:3, n:3,  v:2}),

    (:Station  {name:   "República"}),
    (:Boarding {station:"República", l:3, n:4,  v:1}),
    (:Boarding {station:"República", l:3, n:4,  v:2}),
    (:Boarding {station:"República", l:4, n:10,  v:1}),
    (:Boarding {station:"República", l:4, n:10,  v:2}),

    (:Station  {name:   "Anhangabaú"}),
    (:Boarding {station:"Anhangabaú", l:3, n:5,  v:1}),
    (:Boarding {station:"Anhangabaú", l:3, n:5,  v:2}),

    // Sé (já definido)

    (:Station  {name:   "Pedro II"}),
    (:Boarding {station:"Pedro II", l:3, n:7,  v:1}),
    (:Boarding {station:"Pedro II", l:3, n:7,  v:2}),

    (:Station  {name:   "Brás"}),
    (:Boarding {station:"Brás", l:3, n:8,  v:1}),
    (:Boarding {station:"Brás", l:3, n:8,  v:2}),

    (:Station  {name:   "Mooca"}),
    (:Boarding {station:"Mooca", l:3, n:9,  v:1}),
    (:Boarding {station:"Mooca", l:3, n:9,  v:2}),

    (:Station  {name:   "Belém"}),
    (:Boarding {station:"Belém", l:3, n:10,  v:1}),
    (:Boarding {station:"Belém", l:3, n:10,  v:2}),

    (:Station  {name:   "Tatuapé"}),
    (:Boarding {station:"Tatuapé", l:3, n:11,  v:1}),
    (:Boarding {station:"Tatuapé", l:3, n:11,  v:2}),

    (:Station  {name:   "Carrão"}),
    (:Boarding {station:"Carrão", l:3, n:12,  v:1}),
    (:Boarding {station:"Carrão", l:3, n:12,  v:2}),

    (:Station  {name:   "Penha"}),
    (:Boarding {station:"Penha", l:3, n:13,  v:1}),
    (:Boarding {station:"Penha", l:3, n:13,  v:2}),

    (:Station  {name:   "Vila Matilde"}),
    (:Boarding {station:"Vila Matilde", l:3, n:14,  v:1}),
    (:Boarding {station:"Vila Matilde", l:3, n:14,  v:2}),

    (:Station  {name:   "Esperança"}),
    (:Boarding {station:"Esperança", l:3, n:15,  v:1}),
    (:Boarding {station:"Esperança", l:3, n:15,  v:2}),

    (:Station  {name:   "Patriarca"}),
    (:Boarding {station:"Patriarca", l:3, n:16,  v:1}),
    (:Boarding {station:"Patriarca", l:3, n:16,  v:2}),

    (:Station  {name:   "Artur Alvim"}),
    (:Boarding {station:"Artur Alvim", l:3, n:17,  v:1}),
    (:Boarding {station:"Artur Alvim", l:3, n:17,  v:2}),

    (:Station  {name:   "Itaquera"}),
    (:Boarding {station:"Itaquera", l:3, n:18,  v:1}),
    (:Boarding {station:"Itaquera", l:3, n:18,  v:2}),

    // Linha amarela (L4)
    (:Station  {name:   "Vila Sônia"}),
    (:Boarding {station:"Vila Sônia", l:4, n:1,  v:1}),
    (:Boarding {station:"Vila Sônia", l:4, n:1,  v:2}),

    (:Station  {name:   "Morumbi"}),
    (:Boarding {station:"Morumbi", l:4, n:2,  v:1}),
    (:Boarding {station:"Morumbi", l:4, n:2,  v:2}),

    (:Station  {name:   "Butantã"}),
    (:Boarding {station:"Butantã", l:4, n:3,  v:1}),
    (:Boarding {station:"Butantã", l:4, n:3,  v:2}),

    (:Station  {name:   "Pinheiros"}),
    (:Boarding {station:"Pinheiros", l:4, n:4,  v:1}),
    (:Boarding {station:"Pinheiros", l:4, n:4,  v:2}),

    (:Station  {name:   "Faria Lima"}),
    (:Boarding {station:"Faria Lima", l:4, n:5,  v:1}),
    (:Boarding {station:"Faria Lima", l:4, n:5,  v:2}),

    (:Station  {name:   "Fradique Coutinho"}),
    (:Boarding {station:"Fradique Coutinho", l:4, n:6,  v:1}),
    (:Boarding {station:"Fradique Coutinho", l:4, n:6,  v:2}),

    (:Station  {name:   "Oscar Freire"}),
    (:Boarding {station:"Oscar Freire", l:4, n:7,  v:1}),
    (:Boarding {station:"Oscar Freire", l:4, n:7,  v:2}),

    // Consolação*Paulista (já definido)

    (:Station  {name:   "Higienópolis"}),
    (:Boarding {station:"Higienópolis", l:4, n:9,  v:1}),
    (:Boarding {station:"Higienópolis", l:4, n:9,  v:2}),

    // República (já definido)
    // Luz (já definido)

    // Linha lilás (L5)
    (:Station  {name:   "Capão Redondo"}),
    (:Boarding {station:"Capão Redondo", l:5, n:1,  v:1}),
    (:Boarding {station:"Capão Redondo", l:5, n:1,  v:2}),

    (:Station  {name:   "Campo Limpo"}),
    (:Boarding {station:"Campo Limpo", l:5, n:2,  v:1}),
    (:Boarding {station:"Campo Limpo", l:5, n:2,  v:2}),

    (:Station  {name:   "Vila das Belezas"}),
    (:Boarding {station:"Vila das Belezas", l:5, n:3,  v:1}),
    (:Boarding {station:"Vila das Belezas", l:5, n:3,  v:2}),

    (:Station  {name:   "Giovanni Gronchi"}),
    (:Boarding {station:"Giovanni Gronchi", l:5, n:4,  v:1}),
    (:Boarding {station:"Giovanni Gronchi", l:5, n:4,  v:2}),

    (:Station  {name:   "Santo Amaro"}),
    (:Boarding {station:"Santo Amaro", l:5, n:5,  v:1}),
    (:Boarding {station:"Santo Amaro", l:5, n:5,  v:2}),

    (:Station  {name:   "Largo Treze"}),
    (:Boarding {station:"Largo Treze", l:5, n:6,  v:1}),
    (:Boarding {station:"Largo Treze", l:5, n:6,  v:2}),

    (:Station  {name:   "Adolfo Pinheiro"}),
    (:Boarding {station:"Adolfo Pinheiro", l:5, n:7,  v:1}),
    (:Boarding {station:"Adolfo Pinheiro", l:5, n:7,  v:2}),

    (:Station  {name:   "Alto da Boa Vista"}),
    (:Boarding {station:"Alto da Boa Vista", l:5, n:8,  v:1}),
    (:Boarding {station:"Alto da Boa Vista", l:5, n:8,  v:2}),

    (:Station  {name:   "Borba Gato"}),
    (:Boarding {station:"Borba Gato", l:5, n:9,  v:1}),
    (:Boarding {station:"Borba Gato", l:5, n:9,  v:2}),

    (:Station  {name:   "Brooklin"}),
    (:Boarding {station:"Brooklin", l:5, n:10,  v:1}),
    (:Boarding {station:"Brooklin", l:5, n:10,  v:2}),

    (:Station  {name:   "Eucaliptos"}),
    (:Boarding {station:"Eucaliptos", l:5, n:11,  v:1}),
    (:Boarding {station:"Eucaliptos", l:5, n:11,  v:2}),

    (:Station  {name:   "Moema"}),
    (:Boarding {station:"Moema", l:5, n:12,  v:1}),
    (:Boarding {station:"Moema", l:5, n:12,  v:2}),

    (:Station  {name:   "AACD-Servidor"}),
    (:Boarding {station:"AACD-Servidor", l:5, n:13,  v:1}),
    (:Boarding {station:"AACD-Servidor", l:5, n:13,  v:2}),

    (:Station  {name:   "Hospital São Paulo"}),
    (:Boarding {station:"Hospital São Paulo", l:5, n:14,  v:1}),
    (:Boarding {station:"Hospital São Paulo", l:5, n:14,  v:2}),

    // Santa Cruz (já definido)
    // Chácara Klabin (já definido)

    // Linha Prata (L15)
    
    // Vila Prudente (já definido)

    (:Station  {name:   "Oratório"}),
    (:Boarding {station:"Oratório", l:15, n:2,  v:1}),
    (:Boarding {station:"Oratório", l:15, n:2,  v:2}),

    (:Station  {name:   "São Lucas"}),
    (:Boarding {station:"São Lucas", l:15, n:3,  v:1}),
    (:Boarding {station:"São Lucas", l:15, n:3,  v:2}),
    
    (:Station  {name:   "Camilo Haddad"}),
    (:Boarding {station:"Camilo Haddad", l:15, n:4,  v:1}),
    (:Boarding {station:"Camilo Haddad", l:15, n:4,  v:2}),
    
    (:Station  {name:   "Vila Tolstói"}),
    (:Boarding {station:"Vila Tolstói", l:15, n:5,  v:1}),
    (:Boarding {station:"Vila Tolstói", l:15, n:5,  v:2}),
    
    (:Station  {name:   "Vila União"}),
    (:Boarding {station:"Vila União", l:15, n:6,  v:1}),
    (:Boarding {station:"Vila União", l:15, n:6,  v:2}),
    
    (:Station  {name:   "Jd. Planalto"}),
    (:Boarding {station:"Jd. Planalto", l:15, n:7,  v:1}),
    (:Boarding {station:"Jd. Planalto", l:15, n:7,  v:2}),
    
    (:Station  {name:   "Sapopemba"}),
    (:Boarding {station:"Sapopemba", l:15, n:8,  v:1}),
    (:Boarding {station:"Sapopemba", l:15, n:8,  v:2}),
    
    (:Station  {name:   "Fazenda da Juta"}),
    (:Boarding {station:"Fazenda da Juta", l:15, n:9,  v:1}),
    (:Boarding {station:"Fazenda da Juta", l:15, n:9,  v:2}),
    
    (:Station  {name:   "São Mateus"}),
    (:Boarding {station:"São Mateus", l:15, n:10,  v:1}),
    (:Boarding {station:"São Mateus", l:15, n:10,  v:2}),
    
    (:Station  {name:   "Jardim Colonial"}),
    (:Boarding {station:"Jardim Colonial", l:15, n:11,  v:1}),
    (:Boarding {station:"Jardim Colonial", l:15, n:11,  v:2})
