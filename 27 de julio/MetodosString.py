#upper convierte en mayusculas
#lower convierte en minusculas
#split separa un texto y crea una lista
#join une palabras en una frase
#find encuentra la posicion de una letra
#replace remplaza una palabra de una frase por otra

texto = "esto es un texto en python"

resultado = texto.upper()
print(resultado)
print(texto.lower())
print(texto[2].upper())

resultado2 = texto.split()
print(resultado2)

palabra1 = "aprender"
palabra2= "python"
palabra3 = "es"
palabra4 = "genial"

unir = " ".join([palabra1, palabra2, palabra3, palabra4])
print(unir)

print(texto.find("x"))

print(texto.replace("python", "otro lenguaje"))