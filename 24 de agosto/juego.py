from random import shuffle

opciones = ['-','--','---','----']

def mezclar(lista):
    shuffle(lista)
    return lista

def seleccion():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input('ingrese un numero del 1 al 4: ')
    return int(intento)

def comprobar(lista,intento):
    if lista[intento-1]== '-':
        print('perdiste')
    else:
        print('esta vez te salvaste')
        
opciones_mezcladas = mezclar(opciones)
numero = seleccion()
comprobar(opciones_mezcladas,numero)