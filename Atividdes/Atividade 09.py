"""Verificar Números Pares e Impares com Interrupção

Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para
identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break"""

print("**** **** Verificar Números Pares e Impares com Interrupção **** ****\n\n")
laco = 21
for i in range(1,laco):
    num = int(input("\n\nDigite um numero: "))
    if(num % 2 == 0):
        print(f"O numero {num} e par")
    else:
        print(f"O numero {num} e impar")
    
    if (num == 15):
        print("O programa sera interrompido")
        break
