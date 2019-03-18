#Determinar la cantidad de dígitos de un número ingresado.


def cuenta_digitos(numero):
    numero = str(numero)
    cant  = 0
    for i in range(0, len(numero)):
        if (numero[i] != '.'):
            cant += 1
    return cant


assert(cuenta_digitos(555) == 3)
assert(cuenta_digitos(286.23) == 5)

