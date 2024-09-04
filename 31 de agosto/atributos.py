class Pajaro:
    alas = True
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        
piolin = Pajaro('amarillo', 'canario')

print(piolin.color)
print(piolin.especie)
print(piolin.alas)
print(f"piolin es de color {piolin.color} y es de la especie {piolin.especie}")