def suma(**kwargs):
    resultado = 0
    for clave,valor in kwargs.items():
        #print(f"{clave} = {valor}")
        resultado += valor
    return resultado
    
#print(suma(a=1,b=3,c=5))


def prueba(num1,num2,*args,**kwargs):
    
    print(f'el numero 1 es {num1}')
    print(f'el numero 2 es {num2}')
    
    for arg in args:
        print(f'args= {arg}')
        
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        
        
    print(prueba(15,50,100,200,300,x=1,y=5,z=2))
    