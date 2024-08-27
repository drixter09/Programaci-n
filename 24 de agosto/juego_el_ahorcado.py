from random import choice
palabras = ['lobo','ciudad','portatil','camisa','recreo','sandona','cabeza','tierra','jupiter','paloma','paramo','volcan']
letras_correctas = []
letras_incorrectas = []
vidas = 6
aciertos = 0
juego_terminado = False

def seleccion_palabra(lista_palabras):
    palabra_elegida= choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    
    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_valida=False
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    
    while not es_valida:
        letra_elegida= input('elige una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida)==1:
            es_valida= True
        else:
            print('no ha eleido una letra correcta')
    return letra_elegida

def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []
    
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('_')
            
    print("".join(lista_oculta))
    
def chequear_letra(letra_elegida, palabtra_oculta,vidas,coincidencias):
    fin = False
    
    if letra_elegida in palabtra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
        
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabtra_oculta)
        
    return vidas, fin, coincidencias

def perder():
    print('te has quedado sin vidas')
    print('la palabra correcta era' + palabra)
    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("felicitaciones, has encontrado la palabra")
    return True

palabra, letras_unicas = seleccion_palabra(palabras)

while not juego_terminado:
    print('\n' + '*'*20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('letras_incorrectas' + " ".join(letras_incorrectas))
    print(f'vidas {vidas}')
    print('\n' + '*'*20 + '\n')
    letra = pedir_letra()
    vidas, terminado, aciertos = chequear_letra(letra,palabra,vidas,aciertos)
    juego_terminado = terminado