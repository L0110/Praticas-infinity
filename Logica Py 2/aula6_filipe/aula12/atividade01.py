'''Crie uma hierarquia de classes representando formas geométricas. Comece com uma classe base chamada
"Forma" e, em seguida, crie classes derivadas como "Círculo" e "Retângulo" que herdem da classe base.
Adicione métodos para calcular área e perímetro em cada classe derivada.
'''
import math

class Formas:
    pass

class Retangulos(Formas):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self,):
        return self.base*self.altura
    
    def calcularPerimetro(self):
        return (2*self.base) + (2*self.altura)

class Circulos(Formas):

    def __init__(self, raio):
        self.raio = raio
        self.pi = math.pi
        
    def calcularArea(self):
        return 2*(self.pi*self.raio**2)
    
    def calcularPerimetro(self):
        return 2*self.pi*self.raio
        
bola = Circulos(5)
teclado = Retangulos(2,5)

print("Área Bola: ", bola.calcularArea())
print("Perimetro Bola", bola.calcularPerimetro())

print("Área Teclado: ",teclado.calcularArea())
print("Perimetro Perimetro", teclado.calcularPerimetro())
