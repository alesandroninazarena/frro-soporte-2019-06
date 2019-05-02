# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

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


def buscar_persona(idPersona):
    cSQL = 'SELECT * FROM persona WHERE idPersona = $i'
    value = idPersona
    cursor.execute(cSQL, value)
    resultado = cursor.fetchall()
    if (resultado == []):
        return False
    else:
        return resultado[0]


def actualizar_persona(idPersona, nombre, fechaNac, dni, altura):
    if (buscar_persona(idPersona) == False):
        print('El registro no fue encontrado, id inexistente')
    else:
        print('El registro actual es: ', buscar_persona(idPersona))
        cSQL = 'UPDATE persona SET nombre = %s, fechaNac = %s, dni = %d, altura = %f WHERE idPersona = %d'
        values = (nombre, fechaNac, dni, altura, idPersona)
        cursor.execute(cSQL, values)
        conn.commit()
        print(cursor.rowcount, 'El registro fue actualizado exitosamente')
        if (cursor.rowcount == 0):
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
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()


conn.close()



