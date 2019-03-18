#Determinar la suma de todos los números de 1 a N. N es un número que se ingresa por consola.


def suma_nros(n):
    total = 0
    for i in range(0, n+1):
        total += i
    return total


assert(suma_nros(5) == 15)
assert(suma_nros(3) == 6)
