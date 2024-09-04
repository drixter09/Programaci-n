class Padre:
    def hablar(self):
        print('hola')
        
class Madre:
    def reir(self):
        print('jojojo')
        
    def hablar(self):
        print('que tal')
        
class Hijo(Padre,Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar()
mi_nieto.reir()