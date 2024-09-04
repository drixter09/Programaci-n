class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class Cliente(Persona):
    
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir_cliente(self):
        print(f'''nombre y apellido: {self.nombre} {self.apellido}
                  numero de cuenta: {self.numero_cuenta}
                  balance: {self.balance}''')
        
        
juan = Persona('juan', 'suarez')

print(juan.nombre)
    