class Clientes:
    def __init__(self,nome):
        self.nome = nome
        self.pedidos = []

    def inserir_pedido(self,obj_pedido):
        self.pedidos.append(obj_pedido)

class Pedidos:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

#============================================================
Cleitim = Clientes("Cleitim")

ped1 = Pedidos("Camiseta P", 109.99)
ped3 = Pedidos("Bermuda P", 299.99)
ped7 = Pedidos("Livro Como abrir uma porta", 259.90)

# Associação/relacionamento
Cleitim.inserir_pedido(ped1)
Cleitim.inserir_pedido(ped3)
Cleitim.inserir_pedido(ped7)

#Relatório
total = 0
for pedido in Cleitim.pedidos:
    print(f"Dercrição: {pedido.descricao}, Valor R$ {pedido.valor}")
    total += pedido.valor

print(f"Toral a pagar: R$ {total:.2f}")
