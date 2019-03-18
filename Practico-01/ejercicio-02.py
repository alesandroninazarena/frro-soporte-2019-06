# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.


def mayor(a, b, c):
    if (a > b) and (a > c):
        return a
    elif (b > c) and (b > a):
        return b
    else:
        return c


assert(mayor(4,500,2) == 500)
assert(mayor(-10,-100,0) == 0)
