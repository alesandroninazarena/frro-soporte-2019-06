#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.


def max(a, b):
    if (a >= b):
        return a
    else:
        return b


assert(max(4,10) == 10)
assert(max(5,-10) == 5)
