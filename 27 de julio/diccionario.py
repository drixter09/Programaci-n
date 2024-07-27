diccionario = {"c1":"valor1", "c2":"valor2"}
print(diccionario["c2"])

dic = {"c1":55, "c2":[10,20,30], "c3":{"s1":100, "s2":200}}
resultado = dic["c2"]
print(resultado[1])


resultado2 = dic["c3"]["s2"]
print(resultado2)

dic2 = {"c1":["a","b","c"], "c2":["e","f","g"]}
resultado3 = dic2["c2"][1].upper()
print(resultado3)

dic3 = {1:"a", 2:"b"}
resultado4 = dic3[2] = "c"
print(dic3)
dic3[3] = "f"
print(dic3)