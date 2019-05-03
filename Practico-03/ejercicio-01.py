# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

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

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

conn.close()




