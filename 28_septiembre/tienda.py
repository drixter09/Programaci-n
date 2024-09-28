import mysql.connector

def conectar():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "admin",
        database = "tiendadb"
        )

def registrar_productos(nombre, categoria, cantidad):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "INSERT INTO productos(nombre, categoria, cantidad) VALUES(%s, %s, %s)"
    valores = (nombre, categoria, cantidad)
    cursor.execute(query, valores)
    conexion.commit()
    print(f'{nombre} ha sido agregado correctamente a la lista de productos')
    cursor.close()
    conexion.close()

def ver_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM  productos")
    productos = cursor.fetchall()
    for producto in productos:
        print(producto)
    cursor.close()
    conexion.close()

def actualizar_cantidad(producto_id, nueva_cantidad):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "UPDATE productos SET cantidad = %s WHERE id = %s"
    valores = (nueva_cantidad, producto_id)
    cursor.execute(query, valores)
    conexion.commit()
    print('cantidad actualizada correctamente')
    cursor.close()
    conexion.close()

def actualizar_categoria(producto_id, nueva_categoria):
    conexion = conectar()
    cursor = conexion.cursor()
    query = "UPDATE productos SET categoria = %s WHERE id = %s"
    valores = (nueva_categoria, producto_id)
    cursor.execute(query, valores)
    conexion.commit()
    print('categoria actualizada correctamente')
    cursor.close()
    conexion.close()

def eliminar_producto(id_producto):
    conexion = conectar()
    cursor = conexion.cursor()
    query = f"DELETE FROM productos WHERE id = {id_producto}"
    cursor.execute(query)
    conexion.commit()
    print('El producto ha sido eliminado correctamente')
    cursor.close()
    conexion.close()

def menu():
    while True:
        print("""
              MENÚ
        1- Ver productos
        2- Agregar producto
        3- Actualizar cantidad
        4- Actualizar categoria
        5- Eliminar producto
        6- Salir
        """)
        opcion = input('Escoja una opcion: ')
        match opcion:
            case '1':
                ver_productos()
            case '2':
                nombre = input('Cual es el nombre del nuevo producto: ')
                categoria = input('Cual es su categoria: ')
                cantidad = float(input('Cual es la cantidad: '))
                registrar_productos(nombre, categoria, cantidad)
            case '3':
                id = int(input('Cual es el id del producto al que quiere actualizar la cantidad: '))
                nueva_cantidad = float(input('Cual es la nueva cantidad: '))
                actualizar_cantidad(id,nueva_cantidad)
            case '4':
                id = int(input('Cual es el id del producto al que quiere actualizar la categoria: '))
                nueva_categoria = input('Cual es la nueva categoria: ')
                actualizar_categoria(id,nueva_categoria)
            case '5':
                id_producto = int(input('Cual es el id del producto que desea eliminar: '))
                eliminar_producto(id_producto)
            case '6':
                break
            case _:
                print('Escoja una opcion valida')

menu()