class Calculadoras:
    def __init__(self,fat,fat2):
        self.fator = fat
        self.fator2 = fat2


    def somar(self,fat,fat2 ):
        return fat + fat2
    def subtrair(self,fat,fat2):
        return fat - fat2
    def multiplicar(self,fat,fat2):
        return  fat * fat2
    def dividir(self,fat,fat2):
        return fat / fat2

while True:
    print("1 - Soma")
    print("2 - Subtrais")
    print("3 - Soma")
    print("4 - Soma")

    op = input("Digite Opção: ").strip().upper()
    v1 = input("Digite 1º Valor: ")
    v2 = input("Digite 2º Valor: ")
    
    calculadora = Calculadoras(v1,v2)

    if op =='1':
        print(calculadora.somar())
