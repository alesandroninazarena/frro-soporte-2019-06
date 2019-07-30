# Implementar los metodos de la capa de datos de socios.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio


class DatosSocio(object):

    def __init__(self):
        engine = create_engine('mysql://root:datos@localhost:3306/soporte_practica_03')
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        self.session = DBSession()


    def buscar(self, idSocio):
        socio = self.session.query(Socio).filter_by(id=idSocio).first()
        return socio


    def buscar_dni(self, dniSocio):
        socio = self.session.query(Socio).filter_by(dni=dniSocio).first()
        return socio


    def todos(self):
        socios = self.session.query(Socio).all()
        return socios


    def borrar_todos(self):
        socios = self.todos()
        for s in socios:
            self.session.delete(s)
        self.session.commit()
        if (len(socios) == 0):
            return True
        else:
            return False


    def alta(self, socio):
        self.session.add(socio)
        self.session.commit()
        return socio


    def baja(self, idSocio):
        soc = self.buscar(idSocio)
        if soc is None:
            return False
        elif soc.id == idSocio:
            self.session.delete(soc)
            self.session.commit()
            return True


    def modificacion(self, socio):
        soc = self.buscar(socio.id)
        if soc is None:
            return False
        else:
            self.session.query(Socio).filter_by(id=socio.id).update({Socio.dni:socio.dni, Socio.nombre:socio.nombre, Socio.apellido:socio.apellido})
            self.session.commit()
        return socio




def pruebas():

    datos = DatosSocio()

    # alta
    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id > 0

    # baja
    assert datos.baja(socio.id) == True

    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id) == socio_2

    # buscar dni
    assert datos.buscar_dni(socio_2.dni) == socio_2

    # modificacion
    socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id)
    assert socio_3_modificado.id == socio_3.id
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni == 13264587

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0

    # todos
    assert len(datos.todos()) == 2




if __name__ == '__main__':
    pruebas()



