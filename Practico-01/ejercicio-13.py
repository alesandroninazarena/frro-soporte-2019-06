#Programe una función que determine si un número entero suministrado como argumento es primo.


def es_primo(nro):
    if nro < 2:
        return False
    elif nro == 2:
        return True
    else:
        for i in range(2, nro):
            if nro % i == 0:
                return False
            elif i == nro-1:
                return True

assert(es_primo(4) == False)
assert(es_primo(13) == True)
