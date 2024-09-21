import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin',
    database = 'testdb'
)


my_cursor = mydb.cursor()
my_cursor.execute("SELECT * FROM users")
resultados = my_cursor.fetchall()
for fila in resultados:
    print(f'ID: {fila[0]}, Nombre: {fila[1]}, Email: {fila[2]}, Edad: {fila[3]}')