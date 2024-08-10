lista = ["a",'b','c']

for item in enumerate(lista):
    print(lista)

for indice, elemento in enumerate(lista):
     print(indice, elemento)

mis_tuplas = list(enumerate(lista))
print(mis_tuplas)

#ejercicio

tupla = list(enumerate("python"))
print(tupla)


nombres = ["maria","juan","mario","laura"]
for a, nombre in enumerate(nombres):
     if nombre [0]=="m":
          print(a)