// Cria estações
CREATE
    // Linha azul (L1) e transferências
    (:Blocking {name:"Jabaquara"}),
    (:Boarding {station:"Jabaquara", l:1, n:23, v:1}),
    (:Boarding {station:"Jabaquara", l:1, n:23, v:2}),
    
    (:Blocking {name:"Conceição"}),
    (:Boarding {station:"Conceição", l:1, n:22, v:1}),
    (:Boarding {station:"Conceição", l:1, n:22, v:2}),
    
    (:Blocking {name:"São Judas"}),
    (:Boarding {station:"São Judas", l:1, n:21, v:1}),
    (:Boarding {station:"São Judas", l:1, n:21, v:2}),
    
    (:Blocking {name:"Saúde"}),
    (:Boarding {station:"Saúde", l:1, n:20, v:1}),
    (:Boarding {station:"Saúde", l:1, n:20, v:2}),
    
    (:Blocking {name:"Praça da árvore"}),
    (:Boarding {station:"Praça da árvore", l:1, n:19, v:1}),
    (:Boarding {station:"Praça da árvore", l:1, n:19, v:2}),

    (santa_cruz:Blocking {name:"Santa Cruz"}),
    (:Boarding {station:"Santa Cruz", l:1, n:18, v:1}),
    (:Boarding {station:"Santa Cruz", l:1, n:18, v:2}),
    (:Boarding {station:"Santa Cruz", l:5, n:15, v:1}),
    (:Boarding {station:"Santa Cruz", l:5, n:15, v:2}),

    (:Blocking {name:"Vila Mariana"}),
    (:Boarding {station:"Vila Mariana", l:1, n:17, v:1}),
    (:Boarding {station:"Vila Mariana", l:1, n:17, v:2}),

    (:Blocking {name:"Ana Rosa"}),
    (:Boarding {station:"Ana Rosa", l:1, n:16, v:1}),
    (:Boarding {station:"Ana Rosa", l:1, n:16, v:2}),
    (:Boarding {station:"Ana Rosa", l:2, n:8,  v:1}),
    (:Boarding {station:"Ana Rosa", l:2, n:8,  v:2}),

    (:Blocking {name:"Paraíso"}),
    (:Boarding {station:"Paraíso", l:1, n:15, v:1}),
    (:Boarding {station:"Paraíso", l:1, n:15, v:2}),
    (:Boarding {station:"Paraíso", l:2, n:7,  v:1}),
    (:Boarding {station:"Paraíso", l:2, n:7,  v:2}),

    (:Blocking {name:"Vergueiro"}),
    (:Boarding {station:"Vergueiro", l:1, n:14, v:1}),
    (:Boarding {station:"Vergueiro", l:1, n:14, v:2}),

    (:Blocking {name:"São Joaquim"}),
    (:Boarding {station:"São Joaquim", l:1, n:13, v:1}),
    (:Boarding {station:"São Joaquim", l:1, n:13, v:2}),

    (:Blocking {name:"Liberdade"}),
    (:Boarding {station:"Liberdade", l:1, n:12, v:1}),
    (:Boarding {station:"Liberdade", l:1, n:12, v:2}),

    (:Blocking {name:"Sé"}),
    (:Boarding {station:"Sé", l:1, n:11, v:1}),
    (:Boarding {station:"Sé", l:1, n:11, v:2}),
    (:Boarding {station:"Sé", l:3, n:6,  v:1}),
    (:Boarding {station:"Sé", l:3, n:6,  v:2}),

    (:Blocking {name:"São Bento"}),
    (:Boarding {station:"São Bento", l:1, n:10, v:1}),
    (:Boarding {station:"São Bento", l:1, n:10, v:2}),

    (:Blocking {name:"Luz"}),
    (:Boarding {station:"Luz", l:1, n:9,  v:1}),
    (:Boarding {station:"Luz", l:1, n:9,  v:2}),
    (:Boarding {station:"Luz", l:4, n:11,  v:1}),
    (:Boarding {station:"Luz", l:4, n:11,  v:2}),

    (:Blocking {name:"Tiradentes"}),
    (:Boarding {station:"Tiradentes", l:1, n:8,  v:1}),
    (:Boarding {station:"Tiradentes", l:1, n:8,  v:2}),

    (:Blocking {name:"Armênia"}),
    (:Boarding {station:"Armênia", l:1, n:7,  v:1}),
    (:Boarding {station:"Armênia", l:1, n:7,  v:2}),

    (:Blocking {name:"Tietê"}),
    (:Boarding {station:"Tietê", l:1, n:6,  v:1}),
    (:Boarding {station:"Tietê", l:1, n:6,  v:2}),

    (:Blocking {name:"Carandiru"}),
    (:Boarding {station:"Carandiru", l:1, n:5,  v:1}),
    (:Boarding {station:"Carandiru", l:1, n:5,  v:2}),

    (:Blocking {name:"Santana"}),
    (:Boarding {station:"Santana", l:1, n:4,  v:1}),
    (:Boarding {station:"Santana", l:1, n:4,  v:2}),

    (:Blocking {name:"Jardim São Paulo"}),
    (:Boarding {station:"Jardim São Paulo", l:1, n:3,  v:1}),
    (:Boarding {station:"Jardim São Paulo", l:1, n:3,  v:2}),

    (:Blocking {name:"Parada Inglesa"}),
    (:Boarding {station:"Parada Inglesa", l:1, n:2,  v:1}),
    (:Boarding {station:"Parada Inglesa", l:1, n:2,  v:2}),

    (:Blocking {name:"Tucuruvi"}),
    (:Boarding {station:"Tucuruvi", l:1, n:1,  v:1}),
    (:Boarding {station:"Tucuruvi", l:1, n:1,  v:2}),

    // Linha verde (L2)
    (:Blocking {name:"Vila Madalena"}),
    (:Boarding {station:"Vila Madalena", l:2, n:1,  v:1}),
    (:Boarding {station:"Vila Madalena", l:2, n:1,  v:2}),

    (:Blocking {name:"Sumaré"}),
    (:Boarding {station:"Sumaré", l:2, n:2,  v:1}),
    (:Boarding {station:"Sumaré", l:2, n:2,  v:2}),

    (:Blocking  {name:   "Clínicas"}),
    (:Boarding {station:"Clínicas", l:2, n:3,  v:1}),
    (:Boarding {station:"Clínicas", l:2, n:3,  v:2}),

    (:Blocking  {name:   "Paulista"}),
    (:Boarding {station:"Paulista", l:2, n:4,  v:1}),
    (:Boarding {station:"Paulista", l:2, n:4,  v:2}),
    (:Boarding {station:"Paulista", l:4, n:8,  v:1}),
    (:Boarding {station:"Paulista", l:4, n:8,  v:2}),

    (:Blocking  {name:   "Trianon"}),
    (:Boarding {station:"Trianon", l:2, n:5,  v:1}),
    (:Boarding {station:"Trianon", l:2, n:5,  v:2}),

    (:Blocking  {name:   "Brigadeiro"}),
    (:Boarding {station:"Brigadeiro", l:2, n:6,  v:1}),
    (:Boarding {station:"Brigadeiro", l:2, n:6,  v:2}),

    // Ana Rosa (já definido)
    // Paraíso  (já definido)

    (:Blocking  {name:   "Chácara Klabin"}),
    (:Boarding {station:"Chácara Klabin", l:2, n:9,  v:1}),
    (:Boarding {station:"Chácara Klabin", l:2, n:9,  v:2}),
    (:Boarding {station:"Chácara Klabin", l:5, n:16,  v:1}),
    (:Boarding {station:"Chácara Klabin", l:5, n:16,  v:2}),

    (:Blocking  {name:   "Santos Imigrantes"}),
    (:Boarding {station:"Santos Imigrantes", l:2, n:10,  v:1}),
    (:Boarding {station:"Santos Imigrantes", l:2, n:10,  v:2}),

    (:Blocking  {name:   "Alto do Ipiranga"}),
    (:Boarding {station:"Alto do Ipiranga", l:2, n:11,  v:1}),
    (:Boarding {station:"Alto do Ipiranga", l:2, n:11,  v:2}),

    (:Blocking  {name:   "Sacomã"}),
    (:Boarding {station:"Sacomã", l:2, n:12,  v:1}),
    (:Boarding {station:"Sacomã", l:2, n:12,  v:2}),

    (:Blocking  {name:   "Tamanduateí"}),
    (:Boarding {station:"Tamanduateí", l:2, n:13,  v:1}),
    (:Boarding {station:"Tamanduateí", l:2, n:13,  v:2}),

    (:Blocking  {name:   "Vila Prudente"}),
    (:Boarding {station:"Vila Prudente", l:2, n:14,  v:1}),
    (:Boarding {station:"Vila Prudente", l:2, n:14,  v:2}),
    (:Boarding {station:"Vila Prudente", l:15, n:1,  v:1}),
    (:Boarding {station:"Vila Prudente", l:15, n:1,  v:2}),

    // Linha vermelha (L3)
    (:Blocking  {name:   "Barra Funda"}),
    (:Boarding {station:"Barra Funda", l:3, n:1,  v:1}),
    (:Boarding {station:"Barra Funda", l:3, n:1,  v:2}),

    (:Blocking  {name:   "Mal. Deodoro"}),
    (:Boarding {station:"Mal. Deodoro", l:3, n:2,  v:1}),
    (:Boarding {station:"Mal. Deodoro", l:3, n:2,  v:2}),

    (:Blocking  {name:   "Santa Cecília"}),
    (:Boarding {station:"Santa Cecília", l:3, n:3,  v:1}),
    (:Boarding {station:"Santa Cecília", l:3, n:3,  v:2}),

    (:Blocking  {name:   "República"}),
    (:Boarding {station:"República", l:3, n:4,  v:1}),
    (:Boarding {station:"República", l:3, n:4,  v:2}),
    (:Boarding {station:"República", l:4, n:10,  v:1}),
    (:Boarding {station:"República", l:4, n:10,  v:2}),

    (:Blocking  {name:   "Anhangabaú"}),
    (:Boarding {station:"Anhangabaú", l:3, n:5,  v:1}),
    (:Boarding {station:"Anhangabaú", l:3, n:5,  v:2}),

    // Sé (já definido)

    (:Blocking  {name:   "Pedro II"}),
    (:Boarding {station:"Pedro II", l:3, n:7,  v:1}),
    (:Boarding {station:"Pedro II", l:3, n:7,  v:2}),

    (:Blocking  {name:   "Brás"}),
    (:Boarding {station:"Brás", l:3, n:8,  v:1}),
    (:Boarding {station:"Brás", l:3, n:8,  v:2}),

    (:Blocking  {name:   "Mooca"}),
    (:Boarding {station:"Mooca", l:3, n:9,  v:1}),
    (:Boarding {station:"Mooca", l:3, n:9,  v:2}),

    (:Blocking  {name:   "Belém"}),
    (:Boarding {station:"Belém", l:3, n:10,  v:1}),
    (:Boarding {station:"Belém", l:3, n:10,  v:2}),

    (:Blocking  {name:   "Tatuapé"}),
    (:Boarding {station:"Tatuapé", l:3, n:11,  v:1}),
    (:Boarding {station:"Tatuapé", l:3, n:11,  v:2}),

    (:Blocking  {name:   "Carrão"}),
    (:Boarding {station:"Carrão", l:3, n:12,  v:1}),
    (:Boarding {station:"Carrão", l:3, n:12,  v:2}),

    (:Blocking  {name:   "Penha"}),
    (:Boarding {station:"Penha", l:3, n:13,  v:1}),
    (:Boarding {station:"Penha", l:3, n:13,  v:2}),

    (:Blocking  {name:   "Vila Matilde"}),
    (:Boarding {station:"Vila Matilde", l:3, n:14,  v:1}),
    (:Boarding {station:"Vila Matilde", l:3, n:14,  v:2}),

    (:Blocking  {name:   "Esperança"}),
    (:Boarding {station:"Esperança", l:3, n:15,  v:1}),
    (:Boarding {station:"Esperança", l:3, n:15,  v:2}),

    (:Blocking  {name:   "Patriarca"}),
    (:Boarding {station:"Patriarca", l:3, n:16,  v:1}),
    (:Boarding {station:"Patriarca", l:3, n:16,  v:2}),

    (:Blocking  {name:   "Artur Alvim"}),
    (:Boarding {station:"Artur Alvim", l:3, n:17,  v:1}),
    (:Boarding {station:"Artur Alvim", l:3, n:17,  v:2}),

    (:Blocking  {name:   "Itaquera"}),
    (:Boarding {station:"Itaquera", l:3, n:18,  v:1}),
    (:Boarding {station:"Itaquera", l:3, n:18,  v:2}),

    // Linha amarela (L4)
    (:Blocking  {name:   "Vila Sônia"}),
    (:Boarding {station:"Vila Sônia", l:4, n:1,  v:1}),
    (:Boarding {station:"Vila Sônia", l:4, n:1,  v:2}),

    (:Blocking  {name:   "Morumbi"}),
    (:Boarding {station:"Morumbi", l:4, n:2,  v:1}),
    (:Boarding {station:"Morumbi", l:4, n:2,  v:2}),

    (:Blocking  {name:   "Butantã"}),
    (:Boarding {station:"Butantã", l:4, n:3,  v:1}),
    (:Boarding {station:"Butantã", l:4, n:3,  v:2}),

    (:Blocking  {name:   "Pinheiros"}),
    (:Boarding {station:"Pinheiros", l:4, n:4,  v:1}),
    (:Boarding {station:"Pinheiros", l:4, n:4,  v:2}),

    (:Blocking  {name:   "Faria Lima"}),
    (:Boarding {station:"Faria Lima", l:4, n:5,  v:1}),
    (:Boarding {station:"Faria Lima", l:4, n:5,  v:2}),

    (:Blocking  {name:   "Fradique Coutinho"}),
    (:Boarding {station:"Fradique Coutinho", l:4, n:6,  v:1}),
    (:Boarding {station:"Fradique Coutinho", l:4, n:6,  v:2}),

    (:Blocking  {name:   "Oscar Freire"}),
    (:Boarding {station:"Oscar Freire", l:4, n:7,  v:1}),
    (:Boarding {station:"Oscar Freire", l:4, n:7,  v:2}),

    // Consolação*Paulista (já definido)

    (:Blocking  {name:   "Higienópolis"}),
    (:Boarding {station:"Higienópolis", l:4, n:9,  v:1}),
    (:Boarding {station:"Higienópolis", l:4, n:9,  v:2}),

    // República (já definido)
    // Luz (já definido)

    // Linha lilás (L5)
    (:Blocking  {name:   "Capão Redondo"}),
    (:Boarding {station:"Capão Redondo", l:5, n:1,  v:1}),
    (:Boarding {station:"Capão Redondo", l:5, n:1,  v:2}),

    (:Blocking  {name:   "Campo Limpo"}),
    (:Boarding {station:"Campo Limpo", l:5, n:2,  v:1}),
    (:Boarding {station:"Campo Limpo", l:5, n:2,  v:2}),

    (:Blocking  {name:   "Vila das Belezas"}),
    (:Boarding {station:"Vila das Belezas", l:5, n:3,  v:1}),
    (:Boarding {station:"Vila das Belezas", l:5, n:3,  v:2}),

    (:Blocking  {name:   "Giovanni Gronchi"}),
    (:Boarding {station:"Giovanni Gronchi", l:5, n:4,  v:1}),
    (:Boarding {station:"Giovanni Gronchi", l:5, n:4,  v:2}),

    (:Blocking  {name:   "Santo Amaro"}),
    (:Boarding {station:"Santo Amaro", l:5, n:5,  v:1}),
    (:Boarding {station:"Santo Amaro", l:5, n:5,  v:2}),

    (:Blocking  {name:   "Largo Treze"}),
    (:Boarding {station:"Largo Treze", l:5, n:6,  v:1}),
    (:Boarding {station:"Largo Treze", l:5, n:6,  v:2}),

    (:Blocking  {name:   "Adolfo Pinheiro"}),
    (:Boarding {station:"Adolfo Pinheiro", l:5, n:7,  v:1}),
    (:Boarding {station:"Adolfo Pinheiro", l:5, n:7,  v:2}),

    (:Blocking  {name:   "Alto da Boa Vista"}),
    (:Boarding {station:"Alto da Boa Vista", l:5, n:8,  v:1}),
    (:Boarding {station:"Alto da Boa Vista", l:5, n:8,  v:2}),

    (:Blocking  {name:   "Borba Gato"}),
    (:Boarding {station:"Borba Gato", l:5, n:9,  v:1}),
    (:Boarding {station:"Borba Gato", l:5, n:9,  v:2}),

    (:Blocking  {name:   "Brooklin"}),
    (:Boarding {station:"Brooklin", l:5, n:10,  v:1}),
    (:Boarding {station:"Brooklin", l:5, n:10,  v:2}),

    (:Blocking  {name:   "Eucaliptos"}),
    (:Boarding {station:"Eucaliptos", l:5, n:11,  v:1}),
    (:Boarding {station:"Eucaliptos", l:5, n:11,  v:2}),

    (:Blocking  {name:   "Moema"}),
    (:Boarding {station:"Moema", l:5, n:12,  v:1}),
    (:Boarding {station:"Moema", l:5, n:12,  v:2}),

    (:Blocking  {name:   "AACD-Servidor"}),
    (:Boarding {station:"AACD-Servidor", l:5, n:13,  v:1}),
    (:Boarding {station:"AACD-Servidor", l:5, n:13,  v:2}),

    (:Blocking  {name:   "Hospital São Paulo"}),
    (:Boarding {station:"Hospital São Paulo", l:5, n:14,  v:1}),
    (:Boarding {station:"Hospital São Paulo", l:5, n:14,  v:2}),

    // Santa Cruz (já definido)
    // Chácara Klabin (já definido)

    // Linha Prata (L15)
    
    // Vila Prudente (já definido)

    (:Blocking  {name:   "Oratório"}),
    (:Boarding {station:"Oratório", l:15, n:2,  v:1}),
    (:Boarding {station:"Oratório", l:15, n:2,  v:2}),

    (:Blocking  {name:   "São Lucas"}),
    (:Boarding {station:"São Lucas", l:15, n:3,  v:1}),
    (:Boarding {station:"São Lucas", l:15, n:3,  v:2}),
    
    (:Blocking  {name:   "Camilo Haddad"}),
    (:Boarding {station:"Camilo Haddad", l:15, n:4,  v:1}),
    (:Boarding {station:"Camilo Haddad", l:15, n:4,  v:2}),
    
    (:Blocking  {name:   "Vila Tolstói"}),
    (:Boarding {station:"Vila Tolstói", l:15, n:5,  v:1}),
    (:Boarding {station:"Vila Tolstói", l:15, n:5,  v:2}),
    
    (:Blocking  {name:   "Vila União"}),
    (:Boarding {station:"Vila União", l:15, n:6,  v:1}),
    (:Boarding {station:"Vila União", l:15, n:6,  v:2}),
    
    (:Blocking  {name:   "Jd. Planalto"}),
    (:Boarding {station:"Jd. Planalto", l:15, n:7,  v:1}),
    (:Boarding {station:"Jd. Planalto", l:15, n:7,  v:2}),
    
    (:Blocking  {name:   "Sapopemba"}),
    (:Boarding {station:"Sapopemba", l:15, n:8,  v:1}),
    (:Boarding {station:"Sapopemba", l:15, n:8,  v:2}),
    
    (:Blocking  {name:   "Fazenda da Juta"}),
    (:Boarding {station:"Fazenda da Juta", l:15, n:9,  v:1}),
    (:Boarding {station:"Fazenda da Juta", l:15, n:9,  v:2}),
    
    (:Blocking  {name:   "São Mateus"}),
    (:Boarding {station:"São Mateus", l:15, n:10,  v:1}),
    (:Boarding {station:"São Mateus", l:15, n:10,  v:2}),
    
    (:Blocking  {name:   "Jardim Colonial"}),
    (:Boarding {station:"Jardim Colonial", l:15, n:11,  v:1}),
    (:Boarding {station:"Jardim Colonial", l:15, n:11,  v:2})
