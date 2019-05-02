# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='datos',
                       database='soporte_practica_03')

cursor = conn.cursor()


def agregar_persona(nombre, nacimiento, dni, altura):
    cSQL = 'INSERT INTO persona(nombre, fechaNac, dni, altura) VALUES (%s, %s, %s, %s)'
    values = (nombre, nacimiento, dni, altura)
    cursor.execute(cSQL, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid


def borrar_persona(idPersona):
    cSQL = 'DELETE FROM persona WHERE idPersona = %s'
    value = idPersona
    cursor.execute(cSQL, value)
    conn.commit()
    if mycurr.rowcount == 0:
        return False
    else:
        return True


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper



@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()


conn.close()
