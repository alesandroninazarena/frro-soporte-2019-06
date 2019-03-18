# Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.


def superposicion(lista1, lista2):
    for i in range(0, len(lista1)):
        for j in range(0, len(lista2)):
            if (lista1[i] == lista2[j]):
                return True
    return False

lis1 = ['Hola', 'Chau']
lis2 = ['UTN', 'Soporte a la Gestion de Datos']


assert(superposicion(lis1, lis2) == False)

