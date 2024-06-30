import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

import sys
import os

# Adiciona o diretório atual ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from model.canoas import Canoa

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
    # Consulta para listar todas as canoas
    allCanoas = graphene.List(CanoaType)

    def resolve_allCanoas(self, info):
        return Canoa
        


'''
# Definição de consultas GraphQL
class Query(graphene.ObjectType):
    searchCanoas = graphene.List(CanoaType, tipo=graphene.String(), id_local=graphene.Int())

    def resolve_searchCanoas(self, info, tipo=None, id_local=None):
        query = CanoaType.get_query(info)
        if tipo:
            query = query.filter(Canoa.tipo == tipo)
        if id_local is not None:
            query = query.filter(Canoa.id_local == id_local)
        return query.all()
'''


schema = graphene.Schema(query=Query)
