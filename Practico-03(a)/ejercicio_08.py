# Implementar la funcion listar_pesos, que devuelva el historial de pesos para una persona dada.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# Debe devolver:
# - Lista de (fecha, peso), donde fecha esta representado por el siguiente formato: AAAA-MM-DD.
#   Ejemplo:
#   [
#       ('2018-01-01', 80),
#       ('2018-02-01', 85),
#       ('2018-03-01', 87),
#       ('2018-04-01', 84),
#       ('2018-05-01', 82),
#   ]
# - False en caso de no cumplir con alguna validacion.


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_04 import buscar_persona
from ejercicio_06 import PersonaPeso


Base = declarative_base()


engine = create_engine('mysql://root:datos@localhost:3306/soporte_practica_03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def listar_pesos(idPersona):
    per = buscar_persona(idPersona)
    listaper = []
    if per == False:
        return False
    else:
        pesos = session.query(PersonaPeso).filter_by(idPersona=idPersona).all()
        for p in pesos:
            pp = (p.fecha.strftime("%Y-%m-%d"), p.peso)
            listaper.append(pp)
            return listaper


