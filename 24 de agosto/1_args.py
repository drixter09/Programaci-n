# si no se sabe cuantos argumentos se enviaran a una funcion se utiliza *args

#def suma(num1,num2):
#    return num1 + num2
#
#suma(5,3)
#si se pone otro digito va a poner error ya que la funcion suma solo cuenta comn los argumentos

def suma(*args):
    total= 0
    for a in args:
        total += a
    return total

print(suma(2,5,3,4,6))
