from pydantic import BaseModel
from typing import Optional, List
from model.canoas import *


# BaseModel é a classe base do Pydantic.
# As classes a seguir são modelos de dados baseadas em Pydantic.


# Operações que queremos implementar:
## Criar canoa
## Deletar canoa
## Consultar canoa, informando dados como lista de locais, dono ou tipo de canoa

class SchemaCriacaoCanoa(BaseModel):
    """ 
    Define como uma nova canoa a ser criada deve ser representada, 
    do usuário para a API. 

    Método POST
    """
    nome: str = "E Ala E"
    tipo: str = "OC2"
    dono: str = "Fabio"
    id_local: int = 1

class SchemaExclusaoCanoa(BaseModel):
    """ 
    Define como uma canoa a ser excluída deve ser representada, 
    do usuário para a API. 

    Método DELETE
    """
    id_canoa: int = 1

class SchemaVisualizacaoCanoa(BaseModel):
    """ Define como uma nova canoa recém criada ou uma canoa recém excluída deve ser representada, 
    da API para o usuário.
    """
    id_canoa: int = 1
    nome: str = "E Ala E"
    tipo: str = "OC2"
    dono: str = "Fabio"
    id_local: int = 1


'''
class SchemaBuscaReservaPorUsuario(BaseModel):
    """ 
    Define como deve ser a estrutura que representa a busca, 
    que será feita apenas com base no ID do usuario.

    Método GET
    """
    usuario: int = 21999999999 #Por padrão, sugiro 21999999999    



class SchemaListagemReservas(BaseModel): 
    """ Define como uma listagem de reservas será retornada.
    """
    reservas:List[SchemaVisualizacaoReserva]
'''



def apresenta_canoa(canoa: Canoa):
    """ Retorna uma representação da canoa seguindo o schema definido em
        SchemaVisualizacaoCanoa.
    """
    return {
        "id-canoa": canoa.id_canoa,
        "nome": canoa.nome,
        "tipo": canoa.tipo,
        "dono": canoa.dono,
        "id-local": canoa.id_local
    }

'''
def apresenta_reservas(reservas: list[Reserva]):
    """ Retorna uma representação das reservas seguindo o schema definido em
        SchemaListagemReservas.
    """
    result = []
    for reserva in reservas:
        result.append({
            "id-reserva": reserva.id_reserva,
            "usuario": reserva.id_usuario,
            "canoa": reserva.id_canoa,
            "data": reserva.data  
        })

    return {"reservas": result}
''' 