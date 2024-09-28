import mysql.connector

def conectar():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "admin",
        database = "libreria"
        )

def agregar_libro(titulo, autor, precio):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO libros(titulo, autor, precio) VALUES(%s, %s, %s)"
    valores = (titulo, autor, precio)
    cursor.execute(query, valores)
    conexion.commit()
    print(f'El libro {titulo} ha sido agregado correctamente')
    cursor.close()
    conexion.close()

def obtener_libros():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM  libros")
    libros = cursor.fetchall()
    for libro in libros:
        print(libro)
    cursor.close()
    conexion.close()

def actualizar_precio(libro_id, nuevo_precio):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "UPDATE libros SET precio = %s WHERE id = %s"
    valores = (nuevo_precio, libro_id)
    cursor.execute(query, valores)
    conexion.commit()
    print('Libro actualizado correctamente')
    cursor.close()
    conexion.close()

def eliminar_libro(id_libro):
    conexion = conectar()
    cursor = conexion.cursor()
    query = f"DELETE FROM libros WHERE id = {id_libro}"
    cursor.execute(query)
    conexion.commit()
    print('El libro ha sido eliminado correctamente')
    cursor.close()
    conexion.close()

def menu():
    while True:
        print("""
              MENÚ
        1- Ver libros
        2- Agregar libro
        3- Actualizar precio
        4- Eliminar libro
        5- Salir
        """)
        opcion = input('Escoja una opcion: ')
        match opcion:
            case '1':
                obtener_libros()
            case '2':
                titulo = input('Cual es el titulo del nuevo libro: ')
                autor = input('Quien es el autor del nuevo libro: ')
                precio = float(input('Cual es el precio del nuevo libro: '))
                agregar_libro(titulo, autor, precio)
            case '3':
                id = int(input('Cual es el id del libro al que quiere actualizar el precio: '))
                nuevo_precio = float(input('Cual es el nuevo precio: '))
                actualizar_precio(id,nuevo_precio)
            case '4':
                id_libro = int(input('Cual es el id del libro que desea eliminar: '))
                eliminar_libro(id_libro)
            case '5':
                break
            case _:
                print('Escoja una opcion valida')

menu()