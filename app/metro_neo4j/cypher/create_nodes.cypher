// Via 1 = Via -
// Via 2 = Via +


// Cria estações
CREATE
    // Linha azul (L1) e transferências
    (:Blocking {name:"Jabaquara"}),
    (:Boarding {station:"Jabaquara", l:1, n:23, w:'-'}),
    (:Boarding {station:"Jabaquara", l:1, n:23, w:'+'}),
    
    (:Blocking {name:"Conceição"}),
    (:Boarding {station:"Conceição", l:1, n:22, w:'-'}),
    (:Boarding {station:"Conceição", l:1, n:22, w:'+'}),
    
    (:Blocking {name:"São Judas"}),
    (:Boarding {station:"São Judas", l:1, n:21, w:'-'}),
    (:Boarding {station:"São Judas", l:1, n:21, w:'+'}),
    
    (:Blocking {name:"Saúde"}),
    (:Boarding {station:"Saúde", l:1, n:20, w:'-'}),
    (:Boarding {station:"Saúde", l:1, n:20, w:'+'}),
    
    (:Blocking {name:"Praça da árvore"}),
    (:Boarding {station:"Praça da árvore", l:1, n:19, w:'-'}),
    (:Boarding {station:"Praça da árvore", l:1, n:19, w:'+'}),

    (:Blocking {name:"Santa Cruz"}),
    (:Boarding {station:"Santa Cruz", l:1, n:18, w:'-'}),
    (:Boarding {station:"Santa Cruz", l:1, n:18, w:'+'}),
    (:Boarding {station:"Santa Cruz", l:5, n:15, w:'-'}),
    (:Boarding {station:"Santa Cruz", l:5, n:15, w:'+'}),

    (:Blocking {name:"Vila Mariana"}),
    (:Boarding {station:"Vila Mariana", l:1, n:17, w:'-'}),
    (:Boarding {station:"Vila Mariana", l:1, n:17, w:'+'}),

    (:Blocking {name:"Ana Rosa"}),
    (:Boarding {station:"Ana Rosa", l:1, n:16, w:'-'}),
    (:Boarding {station:"Ana Rosa", l:1, n:16, w:'+'}),
    (:Boarding {station:"Ana Rosa", l:2, n:8,  w:'-'}),
    (:Boarding {station:"Ana Rosa", l:2, n:8,  w:'+'}),

    (:Blocking {name:"Paraíso"}),
    (:Boarding {station:"Paraíso", l:1, n:15, w:'-'}),
    (:Boarding {station:"Paraíso", l:1, n:15, w:'+'}),
    (:Boarding {station:"Paraíso", l:2, n:7,  w:'-'}),
    (:Boarding {station:"Paraíso", l:2, n:7,  w:'+'}),

    (:Blocking {name:"Vergueiro"}),
    (:Boarding {station:"Vergueiro", l:1, n:14, w:'-'}),
    (:Boarding {station:"Vergueiro", l:1, n:14, w:'+'}),

    (:Blocking {name:"São Joaquim"}),
    (:Boarding {station:"São Joaquim", l:1, n:13, w:'-'}),
    (:Boarding {station:"São Joaquim", l:1, n:13, w:'+'}),

    (:Blocking {name:"Liberdade"}),
    (:Boarding {station:"Liberdade", l:1, n:12, w:'-'}),
    (:Boarding {station:"Liberdade", l:1, n:12, w:'+'}),

    (:Blocking {name:"Sé"}),
    (:Boarding {station:"Sé", l:1, n:11, w:'-'}),
    (:Boarding {station:"Sé", l:1, n:11, w:'+'}),
    (:Boarding {station:"Sé", l:3, n:6,  w:'-'}),
    (:Boarding {station:"Sé", l:3, n:6,  w:'+'}),

    (:Blocking {name:"São Bento"}),
    (:Boarding {station:"São Bento", l:1, n:10, w:'-'}),
    (:Boarding {station:"São Bento", l:1, n:10, w:'+'}),

    (:Blocking {name:"Luz"}),
    (:Boarding {station:"Luz", l:1, n:9,  w:'-'}),
    (:Boarding {station:"Luz", l:1, n:9,  w:'+'}),
    (:Boarding {station:"Luz", l:4, n:11,  w:'-'}),
    (:Boarding {station:"Luz", l:4, n:11,  w:'+'}),

    (:Blocking {name:"Tiradentes"}),
    (:Boarding {station:"Tiradentes", l:1, n:8,  w:'-'}),
    (:Boarding {station:"Tiradentes", l:1, n:8,  w:'+'}),

    (:Blocking {name:"Armênia"}),
    (:Boarding {station:"Armênia", l:1, n:7,  w:'-'}),
    (:Boarding {station:"Armênia", l:1, n:7,  w:'+'}),

    (:Blocking {name:"Tietê"}),
    (:Boarding {station:"Tietê", l:1, n:6,  w:'-'}),
    (:Boarding {station:"Tietê", l:1, n:6,  w:'+'}),

    (:Blocking {name:"Carandiru"}),
    (:Boarding {station:"Carandiru", l:1, n:5,  w:'-'}),
    (:Boarding {station:"Carandiru", l:1, n:5,  w:'+'}),

    (:Blocking {name:"Santana"}),
    (:Boarding {station:"Santana", l:1, n:4,  w:'-'}),
    (:Boarding {station:"Santana", l:1, n:4,  w:'+'}),

    (:Blocking {name:"Jardim São Paulo"}),
    (:Boarding {station:"Jardim São Paulo", l:1, n:3,  w:'-'}),
    (:Boarding {station:"Jardim São Paulo", l:1, n:3,  w:'+'}),

    (:Blocking {name:"Parada Inglesa"}),
    (:Boarding {station:"Parada Inglesa", l:1, n:2,  w:'-'}),
    (:Boarding {station:"Parada Inglesa", l:1, n:2,  w:'+'}),

    (:Blocking {name:"Tucuruvi"}),
    (:Boarding {station:"Tucuruvi", l:1, n:1,  w:'-'}),
    (:Boarding {station:"Tucuruvi", l:1, n:1,  w:'+'}),

    // Linha verde (L2)
    (:Blocking {name:"Vila Madalena"}),
    (:Boarding {station:"Vila Madalena", l:2, n:1,  w:'-'}),
    (:Boarding {station:"Vila Madalena", l:2, n:1,  w:'+'}),

    (:Blocking {name:"Sumaré"}),
    (:Boarding {station:"Sumaré", l:2, n:2,  w:'-'}),
    (:Boarding {station:"Sumaré", l:2, n:2,  w:'+'}),

    (:Blocking  {name:   "Clínicas"}),
    (:Boarding {station:"Clínicas", l:2, n:3,  w:'-'}),
    (:Boarding {station:"Clínicas", l:2, n:3,  w:'+'}),

    (:Blocking  {name:   "Paulista"}),
    (:Boarding {station:"Paulista", l:2, n:4,  w:'-'}),
    (:Boarding {station:"Paulista", l:2, n:4,  w:'+'}),
    (:Boarding {station:"Paulista", l:4, n:8,  w:'-'}),
    (:Boarding {station:"Paulista", l:4, n:8,  w:'+'}),

    (:Blocking  {name:   "Trianon"}),
    (:Boarding {station:"Trianon", l:2, n:5,  w:'-'}),
    (:Boarding {station:"Trianon", l:2, n:5,  w:'+'}),

    (:Blocking  {name:   "Brigadeiro"}),
    (:Boarding {station:"Brigadeiro", l:2, n:6,  w:'-'}),
    (:Boarding {station:"Brigadeiro", l:2, n:6,  w:'+'}),

    // Ana Rosa (já definido)
    // Paraíso  (já definido)

    (:Blocking  {name:   "Chácara Klabin"}),
    (:Boarding {station:"Chácara Klabin", l:2, n:9,  w:'-'}),
    (:Boarding {station:"Chácara Klabin", l:2, n:9,  w:'+'}),
    (:Boarding {station:"Chácara Klabin", l:5, n:16,  w:'-'}),
    (:Boarding {station:"Chácara Klabin", l:5, n:16,  w:'+'}),

    (:Blocking  {name:   "Santos Imigrantes"}),
    (:Boarding {station:"Santos Imigrantes", l:2, n:10,  w:'-'}),
    (:Boarding {station:"Santos Imigrantes", l:2, n:10,  w:'+'}),

    (:Blocking  {name:   "Alto do Ipiranga"}),
    (:Boarding {station:"Alto do Ipiranga", l:2, n:11,  w:'-'}),
    (:Boarding {station:"Alto do Ipiranga", l:2, n:11,  w:'+'}),

    (:Blocking  {name:   "Sacomã"}),
    (:Boarding {station:"Sacomã", l:2, n:12,  w:'-'}),
    (:Boarding {station:"Sacomã", l:2, n:12,  w:'+'}),

    (:Blocking  {name:   "Tamanduateí"}),
    (:Boarding {station:"Tamanduateí", l:2, n:13,  w:'-'}),
    (:Boarding {station:"Tamanduateí", l:2, n:13,  w:'+'}),

    (:Blocking  {name:   "Vila Prudente"}),
    (:Boarding {station:"Vila Prudente", l:2, n:14,  w:'-'}),
    (:Boarding {station:"Vila Prudente", l:2, n:14,  w:'+'}),
    (:Boarding {station:"Vila Prudente", l:15, n:1,  w:'-'}),
    (:Boarding {station:"Vila Prudente", l:15, n:1,  w:'+'}),

    // Linha vermelha (L3)
    (:Blocking  {name:   "Barra Funda"}),
    (:Boarding {station:"Barra Funda", l:3, n:1,  w:'-'}),
    (:Boarding {station:"Barra Funda", l:3, n:1,  w:'+'}),

    (:Blocking  {name:   "Mal. Deodoro"}),
    (:Boarding {station:"Mal. Deodoro", l:3, n:2,  w:'-'}),
    (:Boarding {station:"Mal. Deodoro", l:3, n:2,  w:'+'}),

    (:Blocking  {name:   "Santa Cecília"}),
    (:Boarding {station:"Santa Cecília", l:3, n:3,  w:'-'}),
    (:Boarding {station:"Santa Cecília", l:3, n:3,  w:'+'}),

    (:Blocking  {name:   "República"}),
    (:Boarding {station:"República", l:3, n:4,  w:'-'}),
    (:Boarding {station:"República", l:3, n:4,  w:'+'}),
    (:Boarding {station:"República", l:4, n:10,  w:'-'}),
    (:Boarding {station:"República", l:4, n:10,  w:'+'}),

    (:Blocking  {name:   "Anhangabaú"}),
    (:Boarding {station:"Anhangabaú", l:3, n:5,  w:'-'}),
    (:Boarding {station:"Anhangabaú", l:3, n:5,  w:'+'}),

    // Sé (já definido)

    (:Blocking  {name:   "Pedro II"}),
    (:Boarding {station:"Pedro II", l:3, n:7,  w:'-'}),
    (:Boarding {station:"Pedro II", l:3, n:7,  w:'+'}),

    (:Blocking  {name:   "Brás"}),
    (:Boarding {station:"Brás", l:3, n:8,  w:'-'}),
    (:Boarding {station:"Brás", l:3, n:8,  w:'+'}),

    (:Blocking  {name:   "Mooca"}),
    (:Boarding {station:"Mooca", l:3, n:9,  w:'-'}),
    (:Boarding {station:"Mooca", l:3, n:9,  w:'+'}),

    (:Blocking  {name:   "Belém"}),
    (:Boarding {station:"Belém", l:3, n:10,  w:'-'}),
    (:Boarding {station:"Belém", l:3, n:10,  w:'+'}),

    (:Blocking  {name:   "Tatuapé"}),
    (:Boarding {station:"Tatuapé", l:3, n:11,  w:'-'}),
    (:Boarding {station:"Tatuapé", l:3, n:11,  w:'+'}),

    (:Blocking  {name:   "Carrão"}),
    (:Boarding {station:"Carrão", l:3, n:12,  w:'-'}),
    (:Boarding {station:"Carrão", l:3, n:12,  w:'+'}),

    (:Blocking  {name:   "Penha"}),
    (:Boarding {station:"Penha", l:3, n:13,  w:'-'}),
    (:Boarding {station:"Penha", l:3, n:13,  w:'+'}),

    (:Blocking  {name:   "Vila Matilde"}),
    (:Boarding {station:"Vila Matilde", l:3, n:14,  w:'-'}),
    (:Boarding {station:"Vila Matilde", l:3, n:14,  w:'+'}),

    (:Blocking  {name:   "Esperança"}),
    (:Boarding {station:"Esperança", l:3, n:15,  w:'-'}),
    (:Boarding {station:"Esperança", l:3, n:15,  w:'+'}),

    (:Blocking  {name:   "Patriarca"}),
    (:Boarding {station:"Patriarca", l:3, n:16,  w:'-'}),
    (:Boarding {station:"Patriarca", l:3, n:16,  w:'+'}),

    (:Blocking  {name:   "Artur Alvim"}),
    (:Boarding {station:"Artur Alvim", l:3, n:17,  w:'-'}),
    (:Boarding {station:"Artur Alvim", l:3, n:17,  w:'+'}),

    (:Blocking  {name:   "Itaquera"}),
    (:Boarding {station:"Itaquera", l:3, n:18,  w:'-'}),
    (:Boarding {station:"Itaquera", l:3, n:18,  w:'+'}),

    // Linha amarela (L4)
    (:Blocking  {name:   "Vila Sônia"}),
    (:Boarding {station:"Vila Sônia", l:4, n:1,  w:'-'}),
    (:Boarding {station:"Vila Sônia", l:4, n:1,  w:'+'}),

    (:Blocking  {name:   "Morumbi"}),
    (:Boarding {station:"Morumbi", l:4, n:2,  w:'-'}),
    (:Boarding {station:"Morumbi", l:4, n:2,  w:'+'}),

    (:Blocking  {name:   "Butantã"}),
    (:Boarding {station:"Butantã", l:4, n:3,  w:'-'}),
    (:Boarding {station:"Butantã", l:4, n:3,  w:'+'}),

    (:Blocking  {name:   "Pinheiros"}),
    (:Boarding {station:"Pinheiros", l:4, n:4,  w:'-'}),
    (:Boarding {station:"Pinheiros", l:4, n:4,  w:'+'}),

    (:Blocking  {name:   "Faria Lima"}),
    (:Boarding {station:"Faria Lima", l:4, n:5,  w:'-'}),
    (:Boarding {station:"Faria Lima", l:4, n:5,  w:'+'}),

    (:Blocking  {name:   "Fradique Coutinho"}),
    (:Boarding {station:"Fradique Coutinho", l:4, n:6,  w:'-'}),
    (:Boarding {station:"Fradique Coutinho", l:4, n:6,  w:'+'}),

    (:Blocking  {name:   "Oscar Freire"}),
    (:Boarding {station:"Oscar Freire", l:4, n:7,  w:'-'}),
    (:Boarding {station:"Oscar Freire", l:4, n:7,  w:'+'}),

    // Consolação*Paulista (já definido)

    (:Blocking  {name:   "Higienópolis"}),
    (:Boarding {station:"Higienópolis", l:4, n:9,  w:'-'}),
    (:Boarding {station:"Higienópolis", l:4, n:9,  w:'+'}),

    // República (já definido)
    // Luz (já definido)

    // Linha lilás (L5)
    (:Blocking  {name:   "Capão Redondo"}),
    (:Boarding {station:"Capão Redondo", l:5, n:1,  w:'-'}),
    (:Boarding {station:"Capão Redondo", l:5, n:1,  w:'+'}),

    (:Blocking  {name:   "Campo Limpo"}),
    (:Boarding {station:"Campo Limpo", l:5, n:2,  w:'-'}),
    (:Boarding {station:"Campo Limpo", l:5, n:2,  w:'+'}),

    (:Blocking  {name:   "Vila das Belezas"}),
    (:Boarding {station:"Vila das Belezas", l:5, n:3,  w:'-'}),
    (:Boarding {station:"Vila das Belezas", l:5, n:3,  w:'+'}),

    (:Blocking  {name:   "Giovanni Gronchi"}),
    (:Boarding {station:"Giovanni Gronchi", l:5, n:4,  w:'-'}),
    (:Boarding {station:"Giovanni Gronchi", l:5, n:4,  w:'+'}),

    (:Blocking  {name:   "Santo Amaro"}),
    (:Boarding {station:"Santo Amaro", l:5, n:5,  w:'-'}),
    (:Boarding {station:"Santo Amaro", l:5, n:5,  w:'+'}),

    (:Blocking  {name:   "Largo Treze"}),
    (:Boarding {station:"Largo Treze", l:5, n:6,  w:'-'}),
    (:Boarding {station:"Largo Treze", l:5, n:6,  w:'+'}),

    (:Blocking  {name:   "Adolfo Pinheiro"}),
    (:Boarding {station:"Adolfo Pinheiro", l:5, n:7,  w:'-'}),
    (:Boarding {station:"Adolfo Pinheiro", l:5, n:7,  w:'+'}),

    (:Blocking  {name:   "Alto da Boa Vista"}),
    (:Boarding {station:"Alto da Boa Vista", l:5, n:8,  w:'-'}),
    (:Boarding {station:"Alto da Boa Vista", l:5, n:8,  w:'+'}),

    (:Blocking  {name:   "Borba Gato"}),
    (:Boarding {station:"Borba Gato", l:5, n:9,  w:'-'}),
    (:Boarding {station:"Borba Gato", l:5, n:9,  w:'+'}),

    (:Blocking  {name:   "Brooklin"}),
    (:Boarding {station:"Brooklin", l:5, n:10,  w:'-'}),
    (:Boarding {station:"Brooklin", l:5, n:10,  w:'+'}),

    (:Blocking  {name:   "Eucaliptos"}),
    (:Boarding {station:"Eucaliptos", l:5, n:11,  w:'-'}),
    (:Boarding {station:"Eucaliptos", l:5, n:11,  w:'+'}),

    (:Blocking  {name:   "Moema"}),
    (:Boarding {station:"Moema", l:5, n:12,  w:'-'}),
    (:Boarding {station:"Moema", l:5, n:12,  w:'+'}),

    (:Blocking  {name:   "AACD-Servidor"}),
    (:Boarding {station:"AACD-Servidor", l:5, n:13,  w:'-'}),
    (:Boarding {station:"AACD-Servidor", l:5, n:13,  w:'+'}),

    (:Blocking  {name:   "Hospital São Paulo"}),
    (:Boarding {station:"Hospital São Paulo", l:5, n:14,  w:'-'}),
    (:Boarding {station:"Hospital São Paulo", l:5, n:14,  w:'+'}),

    // Santa Cruz (já definido)
    // Chácara Klabin (já definido)

    // Linha Prata (L15)
    
    // Vila Prudente (já definido)

    (:Blocking  {name:   "Oratório"}),
    (:Boarding {station:"Oratório", l:15, n:2,  w:'-'}),
    (:Boarding {station:"Oratório", l:15, n:2,  w:'+'}),

    (:Blocking  {name:   "São Lucas"}),
    (:Boarding {station:"São Lucas", l:15, n:3,  w:'-'}),
    (:Boarding {station:"São Lucas", l:15, n:3,  w:'+'}),
    
    (:Blocking  {name:   "Camilo Haddad"}),
    (:Boarding {station:"Camilo Haddad", l:15, n:4,  w:'-'}),
    (:Boarding {station:"Camilo Haddad", l:15, n:4,  w:'+'}),
    
    (:Blocking  {name:   "Vila Tolstói"}),
    (:Boarding {station:"Vila Tolstói", l:15, n:5,  w:'-'}),
    (:Boarding {station:"Vila Tolstói", l:15, n:5,  w:'+'}),
    
    (:Blocking  {name:   "Vila União"}),
    (:Boarding {station:"Vila União", l:15, n:6,  w:'-'}),
    (:Boarding {station:"Vila União", l:15, n:6,  w:'+'}),
    
    (:Blocking  {name:   "Jd. Planalto"}),
    (:Boarding {station:"Jd. Planalto", l:15, n:7,  w:'-'}),
    (:Boarding {station:"Jd. Planalto", l:15, n:7,  w:'+'}),
    
    (:Blocking  {name:   "Sapopemba"}),
    (:Boarding {station:"Sapopemba", l:15, n:8,  w:'-'}),
    (:Boarding {station:"Sapopemba", l:15, n:8,  w:'+'}),
    
    (:Blocking  {name:   "Fazenda da Juta"}),
    (:Boarding {station:"Fazenda da Juta", l:15, n:9,  w:'-'}),
    (:Boarding {station:"Fazenda da Juta", l:15, n:9,  w:'+'}),
    
    (:Blocking  {name:   "São Mateus"}),
    (:Boarding {station:"São Mateus", l:15, n:10,  w:'-'}),
    (:Boarding {station:"São Mateus", l:15, n:10,  w:'+'}),
    
    (:Blocking  {name:   "Jardim Colonial"}),
    (:Boarding {station:"Jardim Colonial", l:15, n:11,  w:'-'}),
    (:Boarding {station:"Jardim Colonial", l:15, n:11,  w:'+'})
