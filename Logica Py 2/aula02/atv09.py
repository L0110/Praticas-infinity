"""
Escreva um programa que percorra as chaves e valores
de um dicionário separadamente e os exiba.
"""

pessoas = {"nome":["Lucas","Lisa","Monica","Carlos"],
           "idade":[10,20,60,35]}

for k in range(len(pessoas["nome"])):
    print(f'Nome: {pessoas["nome"][k]}')

for v in range(len(pessoas["idade"])):
    print(f'Idade: {pessoas["idade"][v]}')
