from graphene import relay, Int, String, List, ObjectType, Schema, Argument
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from database import Canoa as CanoaDBmodel


# Definição de tipos GraphQL usando SQLAlchemyObjectType
class CanoaSchemaGraphQL(SQLAlchemyObjectType):
    class Meta:
        model = CanoaDBmodel
        #interfaces = (relay.Node,)

    # Mapeamento de campos
    idlocal = Int(source='id_local')  # Mapeando idLocal para id_local no modelo SQLAlchemy
    idcanoa = Int(source='id_canoa')  # Mapeando idCanoa para id_canoa no modelo SQLAlchemy
    nome = String(source='nome') 
    tipo = String(source='tipo') 
    dono = String(source='dono') 



# Definição de consultas GraphQL
from graphene import Argument

class Query(ObjectType):
    canoas = List(CanoaSchemaGraphQL, idlocais=List(Int), tipos=List(String))

    def resolve_canoas(self, info, idlocais=None, tipos=None):
        query = CanoaSchemaGraphQL.get_query(info)  # SQLAlchemy query

        if idlocais is not None:
            query = query.filter(CanoaDBmodel.id_local.in_(idlocais))

        if tipos is not None:
            query = query.filter(CanoaDBmodel.tipo.in_(tipos))    

        return query.all()



schema = Schema(query=Query)