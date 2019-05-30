# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.


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



def borrar_persona(idPersona):
    personas = session.query(Persona)
    for p in personas:
        if p.id == idPersona:
            session.delete(p)
            session.commit()
            q = True
        else:
            q = False
            return q





