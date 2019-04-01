# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.

import random

class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = self.generar_dni()


    def es_mayor_edad(self):
        if (self.edad >= 18):
            return True
        else:
            return False


    def generar_dni(self):
        dni = random.randrange(100000000)
        return dni

    def print_data(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", str(self.edad))
        print("Sexo: ", str(self.sexo))
        print("Peso: ", str(self.peso))
        print("Altura: ", str(self.altura))
        print("DNI: ", str(self.dni))


persona = Persona("Juana", 21, 'M', 60, 1.62)
persona.print_data()
assert(persona.es_mayor_edad() == True)

