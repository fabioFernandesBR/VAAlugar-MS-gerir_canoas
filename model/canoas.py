from sqlalchemy import Column, String, Integer
from model import Base


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

        