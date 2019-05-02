# Implementar la funcion listar_pesos, que devuelva el historial de pesos para una persona dada.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).

# Debe devolver:
# - Lista de (fecha, peso), donde fecha esta representado por el siguiente formato: AAAA-MM-DD.
#   Ejemplo:
#   [
#       ('2018-01-01', 80),
#       ('2018-02-01', 85),
#       ('2018-03-01', 87),
#       ('2018-04-01', 84),
#       ('2018-05-01', 82),
#   ]
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



def listar_pesos(idPersona):
    if (buscar_persona(idPersona) == False):
        return False
    else:
        cSQL = 'SELECT fecha, peso FROM personaPeso WHERE idPersona = %d'
        value = idPersona
        cursor.execute(cSQL, value)
        resultado = cursor.fetchall()
        for i in resultado:
            r = (i[0].strftime('%Y-%m-%d'), i[1])
            lista.append(r)
    return lista



@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()


conn.close()
