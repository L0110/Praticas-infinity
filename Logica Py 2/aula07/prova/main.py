"""
[PYIA-A07] Crie uma função chamada lancar_dados que utilizará o módulo random para simular o 
lançamento de dois dados. Cada dado deve gerar um número aleatório entre 1 e 6. A função deve somar os 
resultados desses dois lançamentos e retornar o valor total.
"""

from funcoes import *

print("-"*60)
print("\t"*1,"Soma de valores aleatorios (01 a 06)")
print("-"*60)

print(f"Resultado: {lancar_dados()}")
