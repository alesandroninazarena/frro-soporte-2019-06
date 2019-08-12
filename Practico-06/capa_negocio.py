# Implementar los metodos de la capa de negocio de socios.

from ejercicio_01 import Socio
from ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, idSocio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar(idSocio)

    def buscar_dni(self, dniSocio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar_dni(dniSocio)

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return self.datos.todos()

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        try:
            if (self.regla_1(socio) == True) and (self.regla_2(socio) == True) and (self.regla_3() == True):
                self.datos.alta(socio)
                return True
        except Exception as ex:
            return False

    def baja(self, idSocio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return self.datos.baja(idSocio)

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        try:
            if (self.regla_2(socio) == True):
                return self.datos.modificacion(socio)
        except LongitudInvalida as ex:
            return False

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        so = self.datos.buscar_dni(socio.dni)
        if so is None:
            return True
        else:
            raise DniRepetido

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if (len(socio.nombre) >= self.MIN_CARACTERES) and (len(socio.nombre) <= self.MAX_CARACTERES):
            if (len(socio.apellido) >= self.MIN_CARACTERES) and (len(socio.apellido) <= self.MAX_CARACTERES):
                return True
            else:
                raise LongitudInvalida
        else:
            raise LongitudInvalida

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if (len(self.datos.todos()) > self.MAX_SOCIOS):
            raise MaximoAlcanzado
        else:
            return True



