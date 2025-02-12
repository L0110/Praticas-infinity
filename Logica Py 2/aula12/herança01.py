class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazerSom(self):
        pass

class Cachorro(Animal):
    def fazerSom(self):
        return "Woof!"
    
class Gato(Animal):
    def fazerSom(self):
        return "Meow!"

rex = Cachorro("Rex")
whiskers = Gato("Whiskers")

print(rex.nome, "faz", rex.fazerSom())
print(whiskers.nome, "faz", whiskers.fazerSom())