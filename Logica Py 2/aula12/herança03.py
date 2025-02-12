from funcs import Automoveis

#chamando a classe mãe/ super classe para a classe filha/ sub classe
class Motocicletas(Automoveis):
    #Atribuição da propriedade "Descanso", exclusiva da classe "Motocicletas"
    def __init__(self, modelo, cor, maxima,descanso):
        super().__init__(modelo, cor, maxima)
        self.descanso = descanso
    def frear(self, velo):
        if(self.velo_atual - velo) >= 0:
            self.velo_atual = self.velo_atual -velo
        if (self.velo_atual > 0):
            return f"Manete acionado \n Velocidade reduzida para {self.velo_atual}"
        else:
            return f"Manete acionado \n Veículo está parado"


cg150 = Motocicletas("CG","Azul", 110, "Lateral")
cg150.acelerar(30)
print("Moto:",cg150.modelo)
print("Velocidade Atual:",cg150.velo_atual)
print(cg150.frear(10))
print(cg150.frear(10))
print(cg150.frear(10))