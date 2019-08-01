# Implementar los casos de prueba descriptos.

import unittest

from ejercicio_01 import Socio
from capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez')

        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)
        valido = Socio(dni=20402685, nombre='Juan', apellido='Perez')

        self.assertTrue(self.ns.regla_1(valido))

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan Fernando Martin', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez Martinez Lopez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        self.assertTrue(self.ns.regla_3())

    def test_baja(self):
        idInv = 10
        self.assertFalse(self.ns.baja(idInv))

        idVal = 86
        self.assertTrue(self.ns.baja(idVal))

    def test_buscar(self):
        id = 10
        self.assertIsNone(self.ns.buscar(id))
        id = 86
        self.assertIsNotNone(self.ns.buscar(id))

    def test_buscar_dni(self):
        dni = 12345678
        self.assertIsNotNone(self.ns.buscar_dni(dni))
        dni = 12578945
        self.assertIsNone(self.ns.buscar_dni(dni))

    def test_todos(self):
        self.assertEqual(len(self.ns.todos()), 6)

    def test_modificacion(self):
        valido = Socio(id=76, dni=78562315, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.modificacion(valido))

        invalido = Socio(id=76, dni=12345679, nombre='Juan', apellido='Perez Martinez Lopez')
        self.assertRaises(LongitudInvalida, self.ns.modificacion, invalido)

