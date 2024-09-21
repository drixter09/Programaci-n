import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin',
    database = 'testdb'
)


my_cursor = mydb.cursor()
sentenciasql = "DELETE FROM users WHERE id_usuario = 2"
my_cursor.execute(sentenciasql)
mydb.commit()
