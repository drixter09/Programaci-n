import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin',
    database = 'testdb'
)


my_cursor = mydb.cursor()
#my_cursor.execute('CREATE TABLE users(id_usuario INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL, edad INT NOT NULL)') 
my_cursor.execute('INSERT INTO users(name, email, edad) VALUES(Esteban, estebang@gmail.com, 21)')
mydb.commit()