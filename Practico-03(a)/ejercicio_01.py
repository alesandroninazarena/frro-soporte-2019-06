# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy import Column, INTEGER, VARCHAR, DATE, FLOAT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Persona(Base):
    __tablename__ = 'persona'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    nombre = Column(VARCHAR(30))
    fechaNac = Column(DATE)
    dni = Column(INTEGER, unique=True)
    altura = Column(FLOAT(3,2))


engine = create_engine('mysql://root:datos@localhost:3306/soporte_practica_03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def crear_tabla():
    Base.metadata.create_all(engine)


def borrar_tabla():
    Persona.__table__.drop()



