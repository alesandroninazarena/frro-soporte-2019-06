# Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

vocales = ['a', 'e', 'i', 'o', 'u']
c = input("Ingrese un caracter: ")

def isvocal(car, lista):
    if (car in lista):
        return True
    else:
        return False

assert(isvocal(c, vocales) == True)



