# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Persona
from ejercicio_04 import buscar_persona

Base = declarative_base()

engine = create_engine('mysql://root:datos@localhost:3306/soporte_practica_03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def actualizar_persona(idPersona, nombre, fechaNac, dni, altura):
    p = buscar_persona(idPersona)
    if p == False:
        return False
    else:
        persona = session.query(Persona).filter_by(id=idPersona).one()
        persona.nombre = nombre
        persona.fechaNac = fechaNac
        persona.dni = dni
        persona.altura = altura
        session.commit()
        return True









