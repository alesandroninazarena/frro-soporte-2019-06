# Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.


def es_palindromo(palabra):
    aux = ""
    for i in range(1, len(palabra)+1):
        aux = aux + palabra[-i]
    if (palabra == aux):
        return ('True')
    else:
        return ('False')


assert(es_palindromo('neuquen') == 'True')
assert(es_palindromo('hola') == 'False')


