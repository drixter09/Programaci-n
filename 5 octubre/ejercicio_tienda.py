import mysql.connector

class Database:
    def __init__(self):
        self.coneccion = mysql.connector.connect(
            user = "root",
            host = "localhost",
            passwd = "admin",
            database = "tienda"
        )
        self.cursor = self.coneccion.cursor()

    def execute_query(self, query, params = None):
        self.cursor.execute(query, params)
        self.coneccion.commit()

    def fetch_query(self, query, params = None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

class Producto:
    def __init__(self):
        self.db = Database()

    def agregar_producto(self, nombre, precio, cantidad):
        query = "INSERT INTO productos(nombre, precio, cantidad) VALUES(%s, %s, %s)"
        self.db.execute_query(query, (nombre, precio, cantidad))
        print(f"{nombre} ha sido agregado a productos")

    def mostrar_productos(self):
        query = "SELECT * FROM productos"
        productos = self.db.fetch_query(query)
        if not productos:
            print("Aún no hay ningun producto registrado")
        else:
            for producto in productos:
                print(f"Id= {producto[0]}, Producto= {producto[1]}, Precio= {producto[2]}$, Cantidad= {producto[3]}")

    def actualizar_cantidad(self, nueva_cantidad, id):
        query = "UPDATE productos SET cantidad = %s WHERE id = %s"
        self.db.execute_query(query, (nueva_cantidad, id))
        print("La cantidad de ha sido actualizada correctamente")

    def eliminar_producto(self, id):
        query = "DELETE FROM productos WHERE id = %s"
        self.db.execute_query(query, (id,))
        print("Producto eliminado correctamente")


def menu():
    manejo_producto = Producto()
    while True:
        print("""
                 Menú Productos
        
        1- Agregar producto
        2- Actualizar cantidad de un producto
        3- Eliminar un producto
        4- Mostrar productos
        5- Salir
        """)
        opcion = input("Elija una opción: ")
        match opcion:
            case "1":
                nombre = input("Nombre del producto: ")
                precio = input("precio del producto: ")
                cantidad = int(input("cantidad: "))
                manejo_producto.agregar_producto(nombre, precio, cantidad)

            case "2":
                id = int(input("Cuál es el ID del producto al que desea actualizar la cantidad: "))
                nueva_cantidad = int(input("Cuál es la nueva cantidad: "))
                manejo_producto.actualizar_cantidad(nueva_cantidad, id)

            case "3":
                id_producto = int(input("Cuál es el ID del producto que desea eliminar: "))
                manejo_producto.eliminar_producto(id_producto)
            
            case "4":
                manejo_producto.mostrar_productos()

            case _ :
                print("Hasta la proxima")
                break

menu()



    