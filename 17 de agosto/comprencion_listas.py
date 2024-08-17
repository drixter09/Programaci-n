palabra = "python"
lista = []

for letra in palabra:
    lista.append(letra)
    print(lista)
    
    
a = [b for b in "programacion"]
print(a)

c = [x for x in range(0,100,5) if x*2>=10]
print(c)

z = [y if y > 10 and y%2==0 else "no" for y in range(0,21)]
print(z)