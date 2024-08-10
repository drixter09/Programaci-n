texto = input("escribe nu texto: ").lower()
letra1 = input("ingrese una letra: ").lower()
letra2 = input("ingrese una segunda letra: ").lower()
letra3 = input("ingrese na tercer letra: ").lower()

lista1 = texto.split(letra1)
cantidad1 = len(lista1)
calculo1 = cantidad1 - 1
print(f"la letra {letra1} aparece {calculo1} veces en su texto")

lista2 = texto.split(letra2)
cantidad2 = len(lista2)
calculo2 = cantidad2 - 1
print(f"la letra {letra2} aparece {calculo2} veces en su texto")

lista3 = texto.split(letra3)
cantidad3 = len(lista3)
calculo3 = cantidad3 - 1
print(f"la letra {letra3} aparece {calculo3} veces en su texto")

palabras = len(texto.split())
print(f"hay {palabras} palabras en tu texto")

primerletra = texto[0]
ultimaletra = texto[-1]
print(f"la primer letra de su texto es \"{primerletra}\" mientras que la ultima letra es \"{ultimaletra}\"")

separar = texto.split()
separar.reverse()
unir = " ".join(separar)
print(f"su texto con las palabras invertidas seria : {unir} ")
verificacion = "python" in texto

if verificacion:
    print("la palabra python si se encuentra en su texto")
else:
    print("la palabra python no se encuentra en su texto")