"""
Verificar Múltiplos de 5 e Parar

Escreva um programa que use um laço for para imprimir números de 1 a 30.
Use uma condicional para verificar se um número é múltiplo de 5 e outro
para verificar se é maior que 20 e interromper o loop com break.
"""
print("Verificar Múltiplos de 5 e Parar")
for i in range (1,31):
    if i%5 == 0:
        print(f"O numero {i} e multiplo de 5")
    if i > 20:
        print("a sequencia chegou ao limite.\n\nO programa sera interrompido")
        break