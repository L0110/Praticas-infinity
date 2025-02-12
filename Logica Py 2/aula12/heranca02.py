class Animais:
    def __init__(self,nome,idade,raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca
    
    def comer(self, comida):
        return f"O {self.nome} está comendo {comida}"
    def fazerSom(self):
        pass

class Gatos(Animais):
    def fazerSom(self):
        return "Miau!"

francisco = Gatos("Francisco", 2, "Pé Duro")

#------------------------------------------------------------------------------

print(francisco.nome)
print(francisco.comer("peixe"))
print(francisco.fazerSom())
