#ejercicio 1

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
        
class Alumno(Persona):
    pass

juan = Alumno('juan', 18)
print(f'mi nombre es {juan.nombre} y tengo {juan.edad} años')

#ejercicio 2

class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
        
class Perro(Mascota):
    pass

doberman = Perro(2, 'Manolo', 4)
print(f'el perro se llama {doberman.nombre}, tiene {doberman.cantidad_patas} patas, y tiene {doberman.edad} años')

#ejercicio 3

class Vehiculo:
    
    def acelerar(self):
        print('el vehiculo ha acelerado')
        
    def frenar(self):
        print('el vehiculo ha frenado')
        
class Automovil(Vehiculo):
    pass

carro = Vehiculo()

carro.acelerar()
carro.frenar()