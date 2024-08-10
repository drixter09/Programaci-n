tupla = (1,2,3,4,5,1)
#print(type(tupla))

MiTupla = (1, "hola", 3.2)

#no se puede modificar
#MiTupla[0] = 7
#print(MiTupla)

t =(1, 2, ("a", "b"), 3)
print(t[2][1])

conversion = list(t)
print(type(conversion))


a, x, y, z = t
print(y)

print(tupla.count(1))