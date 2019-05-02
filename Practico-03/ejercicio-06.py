# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.


import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='datos',
                       database='soporte_practica_03')

cursor = conn.cursor()

def crear_tabla():
    cSQL = 'CREATE TABLE IF NOT EXISTS persona (idPersona INT NOT NULL AUTO_INCREMENT PRIMARY KEY, ' \
           'nombre VARCHAR(30),' \
           'fechaNac DATE, ' \
           'dni INT, ' \
           'altura FLOAT(3,2))
    cursor.execute(cSQL)
    conn.commit()


def borrar_tabla():
    cSQL = 'DROP TABLE persona'
    cursor.execute(cSQL)
    conn.commit()


def crear_tabla_peso():
    cSQL = 'CREATE TABLE IF NOT EXISTS personaPeso(' \
           'idPeso INT NOT NULL AUTO INCREMENT PRIMARY KEY,' \
           'fecha DATE NULL,' \
           'peso FLOAT(5,2),' \
           'FOREING KEY (idPersona) REFERENCES persona(idPersona))'
    cursor.execute(cSQL)


def borrar_tabla_peso():
    cSQL = 'DROP TABLE personaPeso'
    cursor.execute(cSQL)


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper


conn.close()
