"""
Escreva um programa que receba duas listas e calcule
a união dos elementos únicos dessas listas, usando conjuntos.
"""

a = {1, 5, 7, 12, 15, 18}
b = {1, 7, 15, 20, 9, 13}

itens = a.intersection(b)

soma = sum(itens)
print(f"Itens: {itens}")
print(f"Soma: {soma}")