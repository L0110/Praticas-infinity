'''
Crie uma hierarquia de classes que represente veículos. Comece com uma classe base "Veículo" e, em seguida, crie classes derivadas como "Carro"
e "Bicicleta." Adicione métodos para definir atributos, como "cor" e "modelo", e permita a chamada de métodos em cadeia para
configurar esses atributos.
'''


class Veiculos:
    def __init__(self,cor,modelo, tipo):
        self.cor = cor
        self.modelo = modelo
        self.tipo = tipo

class Carros(Veiculos):
    def __init__(self, cor, modelo, tipo):
        super().__init__(cor, modelo, tipo)
        self.lista = dict

class Bicicletas(Veiculos):
    def __init__(self, cor, modelo, tipo):
        super().__init__(cor, modelo, tipo)
        self.lista = dict

while true:
    print("="*60)
    cor = input("Cor do veículo:")
    tipo = input("Tipo do veículo:")
    modelo = input("Modelo do veículo:")
    if (tipo == "carro" or tipo == "CARRO" or tipo == "Carro"):
        tipo = "Carro"
        Carros.lista()