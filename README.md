# VAAlugar-MS-gerir_canoas

Repositório do projeto de Microsserviço (MS) que executa tarefa de gestão das canoas, tais como criar, excluir e consultar.

ATENÇÃO: Docker configurado para rodar na porta 5002.

O que este microsserviço faz
Este MS gerencia as canoas.

Disponibiliza uma rota /criar, para comunicação via REST, usando o método POST. Ao chamar esta rota, informar via JSON: 
O MS vai registrar no banco de dados SQLite (exclusivo deste MS) e retornar a confirmação da criação da canoa ou algum erro.

Com a rota /consultar, diferentes parâmetros podem ser passados via GraphQL, para consulta das canoas disponíveis.

Também disponibiliza a rota /excluir, via REST - DELETE. Ao chamar esta rota, basta informar o id da canoa e o registro correspondente será excluído do banco de dados.

## Parâmetros

## Criação do banco de dados: apenas 1 tabela!
CREATE TABLE canoas (
    id_canoa  INTEGER PRIMARY KEY,
    nome      TEXT,
    tipo      TEXT,
    dono      TEXT,
    id_local  INTEGER NOT NULL
);

## Instalação
Para instalar: use o arquivo requirements.txt para instalar os módulos. No windows: pip install -r requirements.txt Recomendo instalação em um ambiente virtual

Para executar localmente, em ambiente Windows: flask run --host 0.0.0.0 --port 5000 --reload

## Como executar através do Docker
Certifique-se de ter o Docker instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal. Execute como administrador o seguinte comando para construir a imagem Docker:

$ docker build -t ms-canoas .
Uma vez criada a imagem, para executar o container basta executar, como administrador, seguinte o comando:

$ docker run -p 5000:5000 ms-canoas
Uma vez executando, para acessar a API, basta abrir o http://localhost:5002/#/ no navegador.
