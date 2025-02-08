import datetime


dia = (datetime.datetime.now()).day
mes = (datetime.datetime.now()).month
ano = (datetime.datetime.now()).year

print(f"{dia}/{mes}/{ano}")

exit()
class Pessoas:
    def __init__(self, nome, tel, email):
        self.nome = nome
        self.telefone = tel
        self.email = email
        
class Clientes(Pessoas):
    # Atributo de Classe:
    matricula:int = 0
    
    def __init__(self, nome, tel, email=''):
        super().__init__(nome, tel, email )
        self.matricula = 0
                
    def gerar_matricula(self):
        Clientes.matricula
        Clientes.matricula += 1
        self.matricula = Clientes.matricula

class Quartos:
    numero:int = 0
    
    def __init__(self, tipo, diaria):
        self.tipo = tipo
        self.preco = diaria
        self.__disponibilidade = True
    
    def gerar_quarto(self):
        Quartos.numero += 1
        self.numero_quarto = Quartos.numero

class Reservas:
    def __init__(self, obj_cliente, obj_quarto, checkin, checkout):
        self.cliente = obj_cliente
        self.quarto = obj_quarto
        self.checkin = checkin
        self.checkout = checkout
        self.situacao = 'Criada'
        
jorge=Clientes("Jorge Pimenta", "99887766", "jorge@gmail.com")
jorge.gerar_matricula()

q1 = Quartos("Triplex", 100.00)
q2 = Quartos("Suite", 300.00)
q1.gerar_quarto()
print( q1.numero_quarto) #1
q2.gerar_quarto()
print( q2.numero_quarto) #2
r1 = Reservas(jorge, q1, "2025/01/20", "2025/01/30")

print( r1.cliente.telefone )
print( r1.situacao )

data=input("Data: ")
if (data <= r1.checkout) and (data >= r1.checkin):
    r1.quarto.__disponibilidade = False