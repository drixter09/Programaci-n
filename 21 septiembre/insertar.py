import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin',
    database = 'testdb'
)


my_cursor = mydb.cursor()
#sentenciasql = "INSERT INTO users(name, email, edad) VALUES(%s, %s, %s)"
#datos = ('jhon', 'jhon@gmail.com', 30)
#my_cursor.execute(sentenciasql, datos)
#mydb.commit()
#
#my_cursor.execute("INSERT INTO users (name, email, edad) VALUES ('esteban', 'esteban@gmail.com', 21)")
#mydb.commit()

#sentenciasql1 = "INSERT INTO users(name, email, edad) VALUES(%s, %s, %s)"
#datos1 = [('Pablo', 'pablo@gmail.com', 35),
#          ('lucas', 'lucas@gmail.com', 25),
#          ('maria', 'maria@gmail.com', 15)
#          ]
#my_cursor.executemany(sentenciasql1, datos1)
#mydb.commit()
my_cursor.executemany("INSERT INTO users (name, email, edad) VALUES ('sandra', 'sandra@gmail.com', 22), VALUES('julia', 'julia@gmail.com', 41)")
mydb.commit()