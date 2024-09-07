class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    balance = 0
    def __init__(self, nombre, apellido, numero_cuenta):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta

    def __str__(self):
            return f'Nombre: {self.nombre}\nApellido: {self.apellido}\nNumero de cuenta: {self.numero_cuenta}\nBalance: {self.balance}'
    
    def depositar(self):
         cantidad_deposito = int(input('cuanto dinero va a depositar: '))
         self.balance += cantidad_deposito
         print(f'El deposito se ha realizado, su nuevo balance es {self.balance}')
        

    def retirar(self):
        balance_nuevo = realizar_retiro(self.balance)
        self.balance = balance_nuevo
        print(f'El retiro se ha realizado, su nuevo balance es {self.balance}')



def realizar_retiro(balance):
     cantidad_retiro = int(input('cuanto dinero va a retirar: '))
     if cantidad_retiro <= balance:
          return balance - cantidad_retiro
     else:
          print('\nNo tienes saldo suficiente')
          return balance


def inicio():
     nombre = input('Escriba su nombre: ')
     apellido = input('Escriba su apellido: ')
     numero_cuenta = input('Cree un numero de cuenta: ')
     cliente = Cliente(nombre, apellido, numero_cuenta)
     while True:
          print('\nBienvenid@\n\n1- Ver mi informacion\n2- Realizar un deposito\n3- Realizar un retiro\n4- Salir\n')
          respuesta = input('elija una opcion: ')
          if respuesta == '1':
               print(str(cliente))
          elif respuesta == '2':
               cliente.depositar()
          elif respuesta == '3':
               cliente.retirar()
          elif respuesta == '4':
               print('Hasta la proxima')
               break
          else:
               print('Escoja una opcion valida')

inicio()