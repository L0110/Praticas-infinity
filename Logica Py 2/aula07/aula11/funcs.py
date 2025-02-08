# classe começa com letra maiuscula por convenção
# Modelo geral
class Automoveis:
    # Método construtor: responsável por criar um objeto
    # __init__ é padrão que deve ser seguido
    # atributo recebe argumento "self.velo_maxima = maxima"
    def __init__(self, marca, cor, maxima):
        # Atributos da classe:
        self.marca = marca
        self.cor = cor
        self.velo_max = maxima
        self.ligado = False
        self.velo_atual:float = 0

    # comportamentos = métodos
    def ligar_desligar(self):
        if not self.ligado and self.velo_atual == 0:
            self.ligado == True
        elif self.ligado and self.velocidade_atual == 0:
            self.ligado = False
    def acelerar(self, velo):
        if(self.velo_atual + velo) <= self.velo_max:
            self.velo_atual += velo
    
    def frear(self, velo):
        if(self.velo_atual - velo) >= 0:
            self.velo_atual = self.velo_atual -velo