"""
Escreva um programa que recebe um dicionário e uma
lista de chaves como entrada e verifica se todas as
chaves da lista existem no dicionário. A função deve
retornar True se todas as chaves existirem e False caso
contrário.
"""

dicionario = {"A":1,"B":2,"C":3,"D":4}

chaves = ["A","C","F","G"]
i = 0

for k in chaves:
    print(chaves[i]  in dicionario)
    i += 1