#Definir una función que calcule la longitud de una lista o una cadena dada.


dias_semana = ['Lunes', 'Martes', 'Miercoles']
numeros = "123456"


def longitud(cadena):
    lista = list(cadena)
    j = 0
    for i in lista:
        j += 1
    return j

print("Lista:", longitud(dias_semana), "\n")
print("Cadena:", longitud(numeros))






