# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

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


def verificar_fecha(fecha):
    cSQL = 'SELECT max(fecha) from personaPeso'
    cursor.execute(cSQL)
    resultado = cursor.fetchall()
    if (resultado[0][0] == None):
        return True
    elif (resultado[0][0] > fecha.date):
        return False
    else:
        return True



def agregar_peso(idPersona, fecha, peso):
    if (buscar_persona(idPersona) == False):
        print('El id ingresado no existe. Registro no encontrado')
    else:
        if (verificar_fecha(fecha) == False):
            print('Existe un registro con una fecha posterior a la ingresada')
        else:
            cSQL = 'INSERT INTO personaPeso(fecha, peso, idPersona) VALUES (%s, %f, %d)'
            values = (fecha, peso, idPersona)
            cursor.execute(cSQL, values)
            print(cursor.rowcount, 'Registro cargado exitosamente')
            conn.commit()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()


conn.close()




