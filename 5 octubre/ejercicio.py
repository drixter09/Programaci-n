import mysql.connector

class Database:
    def __init__(self):
        self.connexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "admin",
            database = "contactosdb"
        )

        self.cursor = self.connexion.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connexion.commit()

    def fetch_query(self, query, params= None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
    
class Contacto:
    def __init__(self):
        self.db = Database()

    def agregar_contacto(self, nombre, telefono, correo):
        query = "INSERT INTO contactos(nombre, telefono, correo) VALUES(%s, %s, %s)"
        self.db.execute_query(query, (nombre, telefono, correo))
        print(f'{nombre} ha sido agragado a la lista de contactos')

    def listar_contactos(self):
        query = "SELECT * FROM contactos"
        contactos = self.db.fetch_query(query)
        if not contactos:
            print("No hay contactos registrados")
        else:
            for contacto in contactos:
                print(f"Id: {contacto[0]}, Nombre: {contacto[1]}, Telefono: {contacto[2]}, Correo: {contacto[3]}")

    def eliminar_contacto(self, contacto):
        query = "DELETE FROM contactos WHERE id = %s"
        self.db.execute_query(query, (contacto,))
        print(f"Contacto con Id {contacto} ha sido eliminado correctamente")

def menu():
    gestion_contacto = Contacto()
    while True:
        print("""
              Menú de gestión de contactos

        1- Agregar contacto
        2- Mostrar contactos
        3- Eliminar contacto
        4- Salir
        """)
        opcion= input("Seleccione una opción: ")
        match opcion:
            case "1":
                nombre = input("Ingresa un nombre: ")
                telefono = input("Ingresa un telefono: ")
                correo = input("Ingresa un correo: ")
                gestion_contacto.agregar_contacto(nombre, telefono, correo)

            case "2":
                gestion_contacto.listar_contactos()

            case "3":
                id = int(input("Cuál es el ID del contacto que desea eliminar: "))
                gestion_contacto.eliminar_contacto(id)

            case _ :
                print("Hasta la proxima")
                break

menu()
