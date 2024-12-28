"""
Escreva um programa que EXIBA um dicionário contendo
informações de pessoas (nome, idade) e exiba essas informações.
"""

pessoas = {"nome":("Lucas","Lisa","Monica","Carlos"),
           "idade":(10,20,60,35)}

for chave in pessoas.items():
    print(f"Nome: {chave}")
    for valor in pessoas.items():
        print(f"Idade: {valor}")