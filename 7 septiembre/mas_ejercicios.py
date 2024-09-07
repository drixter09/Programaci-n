#ejercicio 1
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}'


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f'Estudiante {estudiante.nombre} ha sido inscrito al curso {self.nombre}')

    def eliminar_estudiante(self, estudiante):
        for nombre in self.estudiantes:
            if nombre == estudiante:
                self.estudiantes.remove(estudiante)
                print('ha sido eliminado')
        

    def mostrar_estudiantes(self):
        if self.estudiantes:
            print(f'Estudiantes inscritos al curso {self.nombre}')
            for estudiante in self.estudiantes:
                print(estudiante)
        else:
                print(f'Aun no hay nadie inscrito al cuerso {self.nombre}')


estudiante1 = Estudiante('Juan Perez', 12, 'septimo')
estudiante2 = Estudiante('Maria Lopez', 13, 'octavo')

curso1 = Curso('Matematicas especiales', 'Jorge Ruiz')

curso1.mostrar_estudiantes()
curso1.agregar_estudiante(estudiante1)
curso1.agregar_estudiante(estudiante2)
curso1.eliminar_estudiante('Maria lopez')
curso1.mostrar_estudiantes()
