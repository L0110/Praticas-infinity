"""
Desenvolva um programa que recebe um dicionário, uma
chave e um valor como entrada e adiciona a chave e o
valor ao dicionário, atualizando o valor se a chave já
existir.
"""
a = {"A": 1, "B": 2, "C": 3}
k = input("insira um identificador: ")
v = input("Insira um valor: ")
if k not in a:
    a[k]=v
else:
    "identificador registrado:"
print(a)