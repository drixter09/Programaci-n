MiLista = ["a","b","c"]
MiLista2 = ["d","e","f"]
MiLista3 = ["c","a","b"]
print(type(MiLista))
print(len(MiLista))

resultado = MiLista[2]
print(resultado)

print(MiLista+MiLista2)
MiLista[0] = "alfa"
print(MiLista)

#append agrega elementos a una lista
#pop quita elementos de una lista
#sort ordena los elementos de una lista

MiLista.append("z")
MiLista.pop(0)
MiLista3.sort()
#MiLista3.reverse()
print(MiLista3)
print(MiLista)