def suma(num1,num2):
    return num1 + num2

resultado = suma(15,10)
print(resultado)

def a(lista):
    nuevaLista = []
    for b in lista:
        if b in range(100,1000):
            nuevaLista.append(b)
        else:
            pass
        print(nuevaLista)
a([123,24,76,345,8765,987,3])