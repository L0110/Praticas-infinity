"""
[PYIA-A05] Crie uma função chamada maior_numero que receberá três números como argumentos. 
Esta função deve comparar os três números e identificar qual deles é o maior. Para isso, utilize 
uma estrutura de controle que verifique qual número é maior que os outros dois. A função deve então retornar 
o maior número encontrado.
"""

#Criação da função
def maior_numero(vlrs):
    maior = 0
    for n in vlrs:
        if n >= maior:
            maior = n
    return maior
#-----------------------
valores = []

print("-"*60)
print("\t"*3,"Maior número")
print("-"*60)

#Entrada de dados
for i in range (1,4):
    num = float(input("Insira um numero: "))
    valores.append(num)

#Impressão na tela
maior = maior_numero(valores)
print(f"O maior numero digitado foi: {maior}")