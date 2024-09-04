class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        
    def piar(self):
        print(f'pio, mi color es {self.color}')
    def volar(self, metros):
            print(f'el pajaro vuela {metros} metros')
            
            
piolin = Pajaro('amarillo', 'canario')

piolin.volar(50)
piolin.piar()


class Persona:
    def __init__(self, color_piel, altura, nombre):
        self.color_piel = color_piel
        self.altura = altura
        self.nombre = nombre
        
    def saludar(self):
        print(f'hola mi nombre es {self.nombre} mido {self.altura}')
        
    def crecer(self):
        self.altura = 2
        print(f'minueva altura es {self.altura} metros')
pablo = Persona('negro', 1.90, 'pablo')

pablo.saludar()
pablo.crecer()
        
    
        