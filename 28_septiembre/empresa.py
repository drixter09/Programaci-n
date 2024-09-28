import mysql.connector

def conectar():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "admin",
        database = "empresa"
        )

def agregar_empleado(nombre, puesto, salario):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO empleados(nombre, puesto, salario) VALUES(%s, %s, %s)"
    valores = (nombre, puesto, salario)
    cursor.execute(query, valores)
    conexion.commit()
    print(f'{nombre} ha sido agregado correctamente a la lista de empleados')
    cursor.close()
    conexion.close()

def ver_empleados():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM  empleados")
    empleados = cursor.fetchall()
    for empleado in empleados:
        print(empleado)
    cursor.close()
    conexion.close()

def actualizar_salario(empleado_id, nuevo_salario):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "UPDATE empleados SET salario = %s WHERE id = %s"
    valores = (nuevo_salario, empleado_id)
    cursor.execute(query, valores)
    conexion.commit()
    print('salario actualizado correctamente')
    cursor.close()
    conexion.close()

def eliminar_empleado(id_empleado):
    conexion = conectar()
    cursor = conexion.cursor()
    query = f"DELETE FROM empleados WHERE id = {id_empleado}"
    cursor.execute(query)
    conexion.commit()
    print('El empleado ha sido eliminado correctamente')
    cursor.close()
    conexion.close()

def menu():
    while True:
        print("""
              MENÚ
        1- Ver empleados
        2- Agregar empleado
        3- Actualizar salario
        4- Eliminar empleado
        5- Salir
        """)
        opcion = input('Escoja una opcion: ')
        match opcion:
            case '1':
                ver_empleados()
            case '2':
                nombre = input('Cual es el nombre del nuevo empleado: ')
                puesto = input('Cual va a ser su puesto: ')
                salario = float(input('Cual es el salario del nuevo empleado: '))
                agregar_empleado(nombre, puesto, salario)
            case '3':
                id = int(input('Cual es el id del empleado al que quiere actualizar el salario: '))
                nuevo_salario = float(input('Cual es el nuevo salario: '))
                actualizar_salario(id,nuevo_salario)
            case '4':
                id_empleado = int(input('Cual es el id del empleado que desea eliminar: '))
                eliminar_empleado(id_empleado)
            case '5':
                break
            case _:
                print('Escoja una opcion valida')

menu()