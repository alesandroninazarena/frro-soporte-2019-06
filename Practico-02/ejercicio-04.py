# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).


import random
import datetime

class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = self.generar_dni()


class Estudiante:

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self, nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas


    def generar_dni(self):
        dni = random.randrange(100000000)
        return dni


    def avance(self):
        porcentaje = float("%.2f" % ((self.cantidad_aprobadas * 100) / self.cantidad_materias))
        return porcentaje


    def edad_ingreso(self):
        edad_ingreso = self.edad - (datetime.datetime.now().year - self.anio)
        return edad_ingreso


estudiante = Estudiante("Juana", 23, 'M', 60, 1.62, "Ing. en Sistemas de Información", 2014, 38, 15)
assert(estudiante.avance() == 39.47 and estudiante.edad_ingreso() == 18)



