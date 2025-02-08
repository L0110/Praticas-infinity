#meta:
"""
"0001":{
    "p01:[4.00, porca, 2]",
    "p02:[10.00, lampada, 1]",
    "p06:[5.00, cola, 1]",
    "p012:[1.00, Parafuso, 10]",
}
"""

class Clientes:
    codigo: int = 0 #Atributo da classe
    dolar:float = 6.15
    codigo_compra = 0
    # Método Construtor:
    def __init__(self, nome, endereco, saldo):
        Clientes.codigo +=1
        self.matricula = Clientes.codigo
        self.nome = nome
        self.endereco = endereco
        self.saldo = saldo
        self.compras:dict = {}
    
    #Criando método de classe conversão
    @classmethod
    def converter(cls, saldo):
        return saldo / Clientes.dolar
    
    #Metrodo string
    def __str__(self):
        return f"Matricula: {self.matricula}, \nNome {self.nome}, \nEndereço: {self.endereco}, \nSaldo R$ {self.saldo:.1f}, | US${ Clientes.converter(self.saldo):.2f}"
    
    
    
    def comprar(self,valor_compra):
        if (valor_compra <= self.saldo):
            self.saldo -= valor_compra
            return self.saldo
        else:
            print("Saldo insuficiente")
            return self.saldo
            
        
    def estorno(self,valor_devolucao):
        self.saldo += valor_devolucao
        return self.saldo
#================================= = ================================= = =================================
cliente_Pedro = Clientes(nome="Pedro Costa",endereco= "Rua ABC, 123",saldo=1200.50)
print(cliente_Pedro.matricula," - ", cliente_Pedro.nome)
cliente_Ana = Clientes("Ana Azedo", "Rua DEF, 456",890.90)
print(cliente_Ana.matricula," - ", cliente_Ana.nome)
print("*"*50)
print(cliente_Pedro)

print("*** compra ***")
print("saldo de ", cliente_Ana.nome)
print("saldo R$", cliente_Ana.saldo)
print(f"Compra -R$ 500,00 :{cliente_Ana.comprar(500)}")
print(f"Compra -R$ 200,00 :{cliente_Ana.comprar(200)}")
print(f"Compra -R$ 500,00 :{cliente_Ana.comprar(500)}")
print(f"Estorno +R$ 200,00 :{cliente_Ana.estorno(200)}")