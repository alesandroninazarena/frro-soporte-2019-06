# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Persona, crear_tabla

Base = declarative_base()

engine = create_engine('mysql://root:datos@localhost:3306/soporte_practica_03')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def agregar_persona(nombre, fechaNac, dni, altura):
    per = Persona()
    per.nombre = nombre
    per.fechaNac = fechaNac
    per.dni = dni
    per.altura = altura
    session.add(per)
    session.commit()
    return per.id






