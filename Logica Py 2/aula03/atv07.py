#07
#REVISÃO
import random as r
import os as c
c.system('clear')

contador = 0
inicio = 0
fim = r.randint(1,99)
passo = r.randint(1,10)
for i in range(inicio,fim,passo):
    print(f"Indice = {contador} | Valor = {i}")
    contador += 1


