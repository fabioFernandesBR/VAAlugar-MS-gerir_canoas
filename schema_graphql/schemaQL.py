import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
import logging
import sys
import os
import model

# Adiciona o diretório atual ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from model.canoas import Canoa


# Configuração do logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Definição de tipos GraphQL usando SQLAlchemyObjectType
class CanoaType(SQLAlchemyObjectType):
    class Meta:
        model = Canoa
        interfaces = (graphene.relay.Node,)

    # Mapeamento de campos
    idLocal = graphene.Int(source='id_local')  # Mapeando idLocal para id_local no modelo SQLAlchemy
    idCanoa = graphene.Int(source='id_canoa')  # Mapeando idCanoa para id_canoa no modelo SQLAlchemy
    nome = graphene.String(source='nome') 
    tipo = graphene.String(source='tipo') 
    dono = graphene.String(source='dono') 

# Definição de consultas GraphQL
class Query(graphene.ObjectType):
    allCanoas = graphene.List(CanoaType)

    def resolve_allCanoas(self, info):
        query = CanoaType.get_query(info)
        canoas = query.all()
        logger.debug("Canoas encontradas: %s", canoas)
        return canoas

schema = graphene.Schema(query=Query)