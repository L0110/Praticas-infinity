#REVISÃO
import random as r
import os as c
c.system('clear')

#01
idade = r.randint(0,99)

if idade < 17:
    print('Você é menor de idade.')
elif idade <=19 and idade>17:
    print('Você é maior de idade.')
else:
    print('Você tem mais de 19 anos!')