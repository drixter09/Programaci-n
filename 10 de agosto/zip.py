nombre = ["juan", "pablo","lorena","nicol"]

edades = [20,25,48,23]

combinados = list(zip(nombre,edades))
print(combinados)

for nombre, edad in combinados:
    print(f"{nombre} tiene {edad} años")