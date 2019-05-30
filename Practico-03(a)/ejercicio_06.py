# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()
# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, INTEGER, DATETIME, FLOAT, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from ejercicio_01 import Persona

Base = declarative_base()


class PersonaPeso(Base):
    __tablename__= 'personaPeso'
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    idPersona = Column(INTEGER, ForeignKey(Persona.id))
    fecha = Column(DATETIME)
    peso = Column(FLOAT(5,2), nullable=False)
    persona = relationship(Persona)



engine = create_engine('mysql://root:datos@localhost:3306/soporte_practica_03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def crear_tabla_peso():
    Base.metadata.create_all(engine)


def borrar_tabla_peso():

    PersonaPeso.__table__.drop(engine)


