import random

def lancar_dados():
    dados = []
    for i in range (1,3):
        num = random.randint(1, 6)
        dados.append(num)
    return sum(dados)
