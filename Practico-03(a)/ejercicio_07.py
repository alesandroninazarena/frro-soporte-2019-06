# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.
# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import PersonaPeso


Base = declarative_base()


engine = create_engine('mysql://root:datos@localhost:3306/soporte_practica_03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def agregar_peso(idPersona, fecha, peso):
    per = buscar_persona(idPersona)
    if per == False:
        return False
    else:
        pesos = session.query(PersonaPeso).filter_by(idPersona=idPersona).all()
        for pe in pesos:
            if pe.fecha >= fecha:
                return False

    pp = PersonaPeso()
    pp.fecha = fecha
    pp.peso = peso
    pp.idPersona = idPersona
    session.add(pp)
    session.commit()
    return pp.id


