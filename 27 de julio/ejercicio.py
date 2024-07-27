nombre = input("escribe tu nombre: ")
ventas = float(input("cuanto has vendido: "))
comision = round((ventas *13) / 100, 2)

x = str(f"hola {nombre} tu comision es de {comision}")
print(x)