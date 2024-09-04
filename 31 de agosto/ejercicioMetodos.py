#ejercicio 1
class Perro:
    def ladrar(self):
        print('Guau!')
        
doberman = Perro()

doberman.ladrar()

#ejercicio 2

class Mago:
    def lanzar_hechizo(self):
        print('Abracadabra!')
        
merlin = Mago()

merlin.lanzar_hechizo()

#ejercicio 3

class Alarma:
    def postergar_alarma(self, tiempo):
        print(f'la alarma ha sido pospuesta {tiempo} minutos')
        
despertador = Alarma()

despertador.postergar_alarma(5)