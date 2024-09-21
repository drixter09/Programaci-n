import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin'
)

print(mydb)

my_cursor = mydb.cursor()
my_cursor.execute('CREATE DATABASE testdb')