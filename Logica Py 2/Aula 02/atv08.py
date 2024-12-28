"""
Escreva um programa que EXIBA um dicionário contendo
informações de pessoas (nome, idade) e exiba essas informações.
"""

pessoas = {"nome":["Lucas","Lisa","Monica","Carlos"],
           "idade":[10,20,60,35]}

print(pessoas)
print(pessoas["nome"])
print(pessoas["idade"])

for i in range(len(pessoas["nome"])):
    print(f"Nome: {pessoas['nome'][i]} - Idade: {pessoas['idade'][i]}")