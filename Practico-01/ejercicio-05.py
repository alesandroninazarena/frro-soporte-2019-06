# Escribir una función multip() que multiplique respectivamente todos los números de una lista. Por ejemplo: multip([1,2,3,4]) debería devolver 24.

numeros = [5.5, 2, 3, 1]


def multip(lista):
    acum = 1
    for i in lista:
        acum *= i
    return acum


assert(multip(numeros) == 33)
