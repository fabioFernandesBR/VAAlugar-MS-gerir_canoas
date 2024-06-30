'''
Criei este arquivo init dentro da pasta database e aqui vou colocar tanto
as funções de uso do banco de dados quanto o modelo SQLAlchemy.
'''

from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (
    create_engine,
    String,
    Integer,
    Column,
    ForeignKey,
    Text
)
import os


# Conectando ao banco de dados
db_path = "database/"

## url de acesso ao banco (essa é uma url de acesso ao sqlite local)
db_url = 'sqlite:///%s/canoas.sqlite' % db_path

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=True)

# Instancia um criador de seção com o banco
Session=scoped_session(sessionmaker(bind=engine))

# Classe Base
### essa função vem do SQLAlchemy, e cria a classe Base, que será usada depois
### como classe-mãe das classes que representarão tabelas do banco de dados.
Base = declarative_base() 
Base.query = Session.query_property()  # cria na classe Base uma propriedade query


# Criando a classe Canoa e a conectando ao banco de dados.
class Canoa(Base):
    __tablename__ = 'canoas'

    id_canoa = Column(Integer, primary_key = True)
    nome = Column(String(50))
    tipo = Column(String(50))
    dono = Column(String(50))
    id_local = Column(Integer)

    def __init__(self, id_local, nome = None, tipo = None, dono = None):
        """
        Cria uma Canoa!

        Arguments:
            id_local
            nome (opcional)
            tipo (opcional)
            dono (opcional)
        """
        self.id_local = id_local
        self.nome = nome
        self.tipo = tipo
        self.dono = dono


# Cria todas as tabelas no banco de dados
Base.metadata.create_all(engine)      