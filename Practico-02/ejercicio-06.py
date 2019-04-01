# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).


import datetime

class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        formato = "%d/%m/%Y %H:%M:%S"
        self.nacimiento= datetime.datetime.strptime(nacimiento, formato)


    def edad(self):
        formato = "%d/%m/%Y %H:%M:%S"
        edad = (datetime.datetime.now() - self.nacimiento).days
        edad = int(edad / 365)
        return edad


persona = Persona("08/06/1996 17:40:00")
assert (persona.edad() == 22)

