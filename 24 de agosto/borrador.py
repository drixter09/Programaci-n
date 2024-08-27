from random import shuffle
lista = ['-','--','---','----']
lista_mezclada = shuffle(lista)
opcion = int(input('escribe un numero del 1 al 4: ')) - 1
#comprobar = lista_mezclada [opcion]
#if comprobar == '-':
#    print('perdiste')
#else:
#    print('esta vez te salvaste')
print(opcion)