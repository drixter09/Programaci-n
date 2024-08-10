#ejercicio 1

alumnos_clase = ["maria", "jose", "carlos", "martina", "isabel","tomas","daniela"]

for saludo in alumnos_clase:
    print("hola " + saludo)

#ejercicio 2

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for suma in lista_numeros:
    suma_numeros +=suma
print(suma_numeros)    

#ejercicio 3

suma_pares = 0
suma_inpares= 0

for ejercicio3 in lista_numeros:
    if ejercicio3 % 2 ==0:
        suma_pares += ejercicio3
    else:
        suma_inpares += ejercicio3
print(f"la suma de numeros pares es {suma_pares} y la suma de impares es igual a {suma_inpares}")