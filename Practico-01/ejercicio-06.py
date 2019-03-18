# Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse".

def inversa(cad):
    aux = ""
    for i in range(1, len(cad)+1):
        aux = aux + cad[-i]
    return aux


assert(inversa('hola') == 'aloh')
