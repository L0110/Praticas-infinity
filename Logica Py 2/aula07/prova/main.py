"""
[PYIA-A07] Crie uma função chamada lancar_dados que utilizará o módulo random para simular o 
lançamento de dois dados. Cada dado deve gerar um número aleatório entre 1 e 6. A função deve somar os 
resultados desses dois lançamentos e retornar o valor total.
"""
#importacao da funcao "Lancar_dados"
from funcoes import lancar_dados
#---------------------------------
print("-"*60)
print("\t"*1,"Soma de valores aleatorios (01 a 06)")
print("-"*60)
#Impressao na tela
print(f"Resultado: {lancar_dados()}")
