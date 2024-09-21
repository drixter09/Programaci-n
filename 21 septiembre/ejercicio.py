import mysql.connector

base_datos = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin'
)

cursor = base_datos.cursor()

cursor.execute("CREATE DATABASE universidad")
base_datos.commit()


base_datos = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin',
    database = 'universidad'
)

cursor = base_datos.cursor()

cursor.execute("CREATE TABLE estudiantes(id_estudiante INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(30) NOT NULL, edad INT NOT NULL")
base_datos.commit()

cursor.execute("CREATE TABLE cursos(id_curso INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(30) NOT NULL, creditos INT NOT NULL)")
base_datos.commit()

cursor.execute("""
INSERT INTO estudiantes(nombre, edad)
VALUES ('juan', 21),
       ('pablo', 22),
       ('maria',20)
""")

base_datos.commit()

cursor.execute("""
INSERT INTO cursos(nombre, creditos)
VALUES ('matematicas', 20),
       ('ingles', 25),
       ('ciencias', 30)
""")

base_datos.commit()

cursor.close()
base_datos.close()
