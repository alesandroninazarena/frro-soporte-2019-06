# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Persona

Base = declarative_base()

engine = create_engine('mysql://root:datos@localhost:3306/soporte_practica_03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def buscar_persona(idPersona):
    personas = session.query(Persona)
    for p in personas:
        if p.id == idPersona:
            return (p.id, p.nombre, p.fechaNac, p.dni, p.altura)
        else:
            return False



