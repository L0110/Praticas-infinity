"""
REVISÃO: HEREANÇA E POLIMORFISMO

HERANÇA: QUANDO UMA CLASSE HERDA ATRIBUTOS E METODOS DE UMA SUPER CLASE

POLIMORFISMO: MÉTODOS (FUNÇÕES) EM CLASSES PYTHON
QUE TEM A MESMA ASSINATURA, MAS COM COMORTAMENTOS DISTINTOS.
"""

#ENCAPSULAMENTO: (conexção fraca. roteção assiva contra erros acidentais)
class Contas_corrente:
    def __init__(self, numero, nome):
        self.conta = numero
        self.correntista = nome
        self.__saldo = 0 

    #DECORATOR: todo comando com @ é chamado decorador: ele transforma funções em variaveis
    @property
    def saldo(self): #Getter
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor): #Setter
        if ((self.__saldo + valor) >= 0):
            self.__saldo += valor
        else:
            print(f"Saldo Insuficiente")         
    
#===========================================================

jorge_cc = Contas_corrente("0001-1","Jorge Pimenta")
print(jorge_cc.correntista)

print(jorge_cc.saldo) #0 - Getter

jorge_cc.saldo = 1_000 # Setter
print(jorge_cc.saldo) #0 - Getter

jorge_cc.saldo = (-1_000_000) # Setter
print(jorge_cc.saldo) #0 - Getter

