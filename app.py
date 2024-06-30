from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from flask_graphql import GraphQLView
from sqlalchemy.exc import IntegrityError

from model import Session, Canoa
from logger import logger
from schemas import *
from schema_graphql.schemaQL import schema

from flask_cors import CORS

info = Info(title="VAAlugar-MS-canoas", version="0.1.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
criacao_canoa_tag = Tag(name="Criação de Canoa", description="Registro de canoas para locação")
exclusao_canoa_tag = Tag(name="Exclusão de Canoa", description="Exclusão de canoas para locação")
consulta_reserva_tag = Tag(name="Consulta de Reserva", description="Consulta de reservas de canoas para locação")
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação."""
    return redirect('/openapi')

@app.post('/criar', tags=[criacao_canoa_tag],
          responses={"200": SchemaVisualizacaoCanoa, "409": SchemaMensagemErro, "400": SchemaMensagemErro})
def cria_reserva(form: SchemaCriacaoCanoa):
    """Cria uma canoa

    Retorna uma representação da canoa criada. 
    """
    logger.debug(f"Recebido dados para criação de canoa: {form}")
    canoa = Canoa(
        id_local=form.id_local, 
        nome=form.nome, 
        tipo=form.tipo, 
        dono=form.dono
    )
    logger.debug(f"Canoa criada: {canoa}")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando reserva
        session.add(canoa)
        # efetivando o comando de criação da reserva na tabela
        session.commit()
        logger.debug(f"Reserva persistida no banco de dados: {canoa}")
        return apresenta_canoa(canoa), 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível criar canoa : {e}"
        logger.warning(f"Erro ao criar reserva, {error_msg}")
        return {"message": error_msg}, 400

@app.delete('/excluir', tags=[exclusao_canoa_tag],
            responses={"200": SchemaVisualizacaoCanoa, "404": SchemaMensagemErro, "400": SchemaMensagemErro})
def exclui_canoa(form: SchemaExclusaoCanoa):
    """Exclui uma canoa

    Retorna uma representação da canoa excluída. 
    """
    logger.debug(f"Recebido dados para exclusão de canoa: {form}")
    try:
        # criando conexão com a base
        session = Session()
        # buscando a canoa a ser excluída
        canoa = session.query(Canoa).filter_by(id_canoa=form.id_canoa).first()
        if canoa is None:
            error_msg = "Canoa não encontrada"
            logger.warning(f"Erro ao excluir canoa, {error_msg}")
            return {"message": error_msg}, 404

        logger.debug(f"Canoa encontrada: {canoa}")

        # excluindo a canoa
        session.delete(canoa)
        # efetivando a exclusão no banco de dados
        session.commit()
        logger.debug(f"Canoa excluída do banco de dados: {canoa}")
        return apresenta_canoa(canoa), 200
    except Exception as e:
        # caso um erro fora do previsto
        session.rollback()  # reverte quaisquer mudanças no banco de dados
        error_msg = f"Não foi possível excluir a canoa: {e}"
        logger.warning(f"Erro ao excluir canoa, {error_msg}")
        return {"message": error_msg}, 400
    finally:
        session.close()

# Configuração do endpoint GraphQL
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Habilita a interface GraphiQL para testar queries
    )
)

if __name__ == '__main__':
    app.run(debug=True)