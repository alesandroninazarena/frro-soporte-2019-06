# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)


from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, INTEGER, VARCHAR



Base = declarative_base()


class Socio(Base):
    __tablename__ = 'socios'
    id = Column(INTEGER, primary_key=True, autoincrement=True, unique=True)
    dni = Column(INTEGER, unique=True)
    nombre = Column(VARCHAR(250))
    apellido = Column(VARCHAR(250))



engine = create_engine('mysql://root:datos@localhost:3306/soporte_practica_03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

Base.metadata.create_all(engine)

