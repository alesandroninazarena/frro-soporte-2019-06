# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

import random

class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = self.generar_dni()

    def generar_dni(self):
        dni = random.randrange(100000000)
        return dni


class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self, nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas



def organizar_estudiantes(estudiantes):
    carreras = []
    alumnos = {}

    for i in estudiantes:
        if (i.carrera not in carreras):
            carreras.append(i.carrera)

    for j in carreras:
        cant_alumnos = 0
        for k in estudiantes:
            if (k.carrera ==  j):
                cant_alumnos += 1
                alumnos[k.carrera] = cant_alumnos

    return alumnos



e1 = Estudiante("Juana", 23, 'M', 60, 1.62, "Ing. en Sistemas de Información", 2014, 38, 15)
e2 = Estudiante("Martin", 21, 'H', 75, 1.84, "Ing. en Sistemas de Información", 2016, 38, 7)
e3 = Estudiante("Matias", 25, 'H', 82, 1.78, "Ing. Mecánica", 2013, 36, 20)
e4 = Estudiante("Lucía", 19, 'M', 65, 1.65, 'Ing. Química', 2018, 40, 7)
e5 = Estudiante("Tomas", 23, 'H', 78, 1.73, 'Ing. Química', 2014, 40, 32)
e6 = Estudiante("Laura", 28, 'M', 74, 1.59, "Ing. en Sistemas de Información", 2010, 38, 27)

estudiantes = [e1, e2, e3, e4, e5, e6]

dic = organizar_estudiantes(estudiantes)
assert(list(dic.keys()) == ["Ing. en Sistemas de Información", "Ing. Mecánica", "Ing. Química"] and list(dic.values()) == [3, 1, 2])



