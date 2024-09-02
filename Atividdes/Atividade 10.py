"""
Contar Números Positivos e Negativos
Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos
são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break.
"""

print("Contar Números Positivos e Negativos")
pos = 0
neg = 0
for i in range (10):
    num = int(input("Insira um numero: "))
    if num > 0:
        pos += 1
    elif num == 0:
        print("A repeticao foi interrompida")
        break
    else:
        neg += 1

print("###### Contagem de numeros ######")
print(f"Numeros positivos: {pos}")
print(f"Numeros negativos: {neg}")
