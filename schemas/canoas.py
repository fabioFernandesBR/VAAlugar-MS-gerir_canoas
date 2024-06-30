from pydantic import BaseModel
from typing import Optional, List
from database import Canoa


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
