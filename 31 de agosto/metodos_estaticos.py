class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        
    def piar(self):
        print(f'pio, mi color es {self.color}')
    def volar(self, metros):
            print(f'el pajaro vuela {metros} metros')
            
    @staticmethod
    def mirar():
        print('el pajaro mira')
            
            
piolin = Pajaro('amarillo', 'canario')

piolin.volar(50)
piolin.piar()
Pajaro.mirar()
