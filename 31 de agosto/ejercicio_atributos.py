#ejercicio 1

class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
        

casa_blanca = Casa('blanca', '4')


#ejercicio 2

class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color
    
cubo_rojo = Cubo('rojo')

#ejercicio 3

class Personaje:
    real = False
    def __init__(self, magico, especie, edad):
        self.magico = magico
        self.especie = especie
        self.edad = edad
        
harry_potter = Personaje(True, 'humano', 17)