# VAAlugar-MS-gerir_canoas

Repositório do projeto de Microsserviço (MS) que executa tarefa de gestão das canoas, tais como criar, excluir e consultar.

ATENÇÃO: Docker configurado para rodar na porta 5002.

O que este microsserviço faz
Este MS gerencia as canoas.

Disponibiliza uma rota /criar, para comunicação via REST, usando o método POST. Ao chamar esta rota, informar via JSON: 
O MS vai registrar no banco de dados SQLite (exclusivo deste MS) e retornar a confirmação da criação da canoa ou algum erro.

Também disponibiliza a rota /excluir, via REST - DELETE. Ao chamar esta rota, basta informar o id da canoa e o registro correspondente será excluído do banco de dados.

As consultas são disponibilizadas por meio de um endpoint para graphQL:
- query se chama canoas.
- 2 critérios de busca são habilitados: idlocais e tipos. Ambos são habilitados como listas, de modo que cada um pode buscar por mais de um valor.
- Os idlocais são os locais onde as canoas estão disponibilizadas. São valores inteiros.
- Os tipos são as características das canoas, como OC2, OC4 e OC6. São strings.
- As variáveis disponíveis para retorno são idlocal, idcanoa, nome (da canoa), tipo e dono.
- A documentação do graphiQL mostra o seguinte:
-     canoas(idlocais: [Int]tipos: [String]): [CanoaSchemaGraphQL], onde [CanoaSchemaGraphQL] é:
-     idCanoa: ID! (interno do graphQL - NÃO USE ESSE)
-     nome: String
-     tipo: String
-     dono: String
-     idlocal: Int
-     idcanoa: Int

# Parâmetros
## Criação de canoa
http://localhost:5002/criar
### Chamada REST
curl -X 'POST' \
  'http://127.0.0.1:5002/criar' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'dono=Malu' \
  -F 'id_local=8' \
  -F 'nome=Luna' \
  -F 'tipo=OC2'

### Resposta JSON
{
  "dono": "Malu",
  "id-canoa": 11,
  "id-local": 8,
  "nome": "Luna",
  "tipo": "OC2"
}

## Exclusão de canoa
http://localhost:5002/excluir
### Chamada REST
curl -X 'DELETE' \
  'http://127.0.0.1:5002/excluir' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -d '{
  "id_canoa": "5"
}'

### Resposta JSON
{
  "dono": "Fabio",
  "id-canoa": 5,
  "id-local": 12,
  "nome": "Antares",
  "tipo": "OC1"
}
 access-control-allow-origin: http://127.0.0.1:5002 
 connection: close 
 content-length: 74 
 content-type: application/json 
 date: Mon,01 Jul 2024 00:13:10 GMT 
 server: Werkzeug/3.0.3 Python/3.12.4 
 vary: Origin 

 ## Consultas
 Como usamos o graphql, o usuário tem flexibilidade para especificar quais atributos ele quer receber. A seguir exemplos:

 ### Retorna todas as informações de todas as canoas disponíveis:
 {
  canoas{
    idcanoa
    nome
    tipo
    dono
    idlocal
  }
}

### Retorna apenas nome, tipo e idlocal de todas as canoas disponíveis:
 {
  canoas{
    nome
    tipo
    idlocal
  }
}

### Retorna apenas nome, tipo e idlocal de todas as canoas disponíveis cujo tipo seja "OC1"ou "OC2":
{
  canoas(tipos: ["OC1", "OC2"]){
    idcanoa
    nome
    tipo
    dono
    idlocal
  }
}

### Retorna apenas nome, tipo e idlocal de todas as canoas disponíveis cujo tipo seja "OC1"ou "OC2" E idlocal seja 1, 8 ou 12:
{
  canoas(tipos: ["OC1", "OC2"], idlocais: [1,8,12]){
    idcanoa
    nome
    tipo
    dono
    idlocal
  }
}

### Retorno
Exemplo de retorno para esta última query:
{
  "data": {
    "canoas": [
      {
        "idcanoa": 1,
        "nome": "E Ala E",
        "tipo": "OC2",
        "dono": "Fabio",
        "idlocal": 1
      },
      {
        "idcanoa": 8,
        "nome": "Fredingo Lingo",
        "tipo": "OC2",
        "dono": "Fred",
        "idlocal": 1
      },
      {
        "idcanoa": 9,
        "nome": "Nossa Química",
        "tipo": "OC2",
        "dono": "Vanessa",
        "idlocal": 12
      },
      {
        "idcanoa": 10,
        "nome": "Malu",
        "tipo": "OC2",
        "dono": "Malu",
        "idlocal": 1
      },
      {
        "idcanoa": 11,
        "nome": "Luna",
        "tipo": "OC2",
        "dono": "Malu",
        "idlocal": 8
      }
    ]
  }
}

# Criação do banco de dados: apenas 1 tabela!
CREATE TABLE canoas (
    id_canoa  INTEGER PRIMARY KEY,
    nome      TEXT,
    tipo      TEXT,
    dono      TEXT,
    id_local  INTEGER NOT NULL
);

# Instalação
Para instalar: use o arquivo requirements.txt para instalar os módulos. No windows: pip install -r requirements.txt Recomendo instalação em um ambiente virtual

Para executar localmente, em ambiente Windows: flask run --host 0.0.0.0 --port 5000 --reload

## Como executar através do Docker
Certifique-se de ter o Docker instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal. Execute como administrador o seguinte comando para construir a imagem Docker:

$ docker build -t ms-canoas .
Uma vez criada a imagem, para executar o container basta executar, como administrador, seguinte o comando:

$ docker run -p 5002:5000 ms-canoas
Uma vez executando, para acessar a API, basta abrir o http://localhost:5002/ no navegador para acessar o Swagger e testar as rotas REST e http://localhost:5002/graphql para acessar o graphiql e testar a query via GraphQL. 
