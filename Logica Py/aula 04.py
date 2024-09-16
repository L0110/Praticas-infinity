"""Atividade 01:
Tabuada de um Número:
Faça um programa que solicite um número ao usuário e use
um laço for para exibir a tabuada desse número (de 1 a 10)."""

print("- - - - Tabuada - - - -")
num = float(input("Insira um número: "))

fim = "S"
op = 1
while fim == "S":
    while (op >0  and op <5):
        print("\n\nOperação:\n01) Multiplicação (x)\n02)Divisão (/)\n03)Soma (+)\n04)subtração (-)")
        op = int(input("opção: "))
        
        if op == 1:
            for i in range (1,11):
                print(f"{i} X {num} = {i*num}")
                
        elif op == 2:
            for i in range (1,11):
                print(f"{i} / {num}  = {i/num}")
                
        elif op == 3:
            for i in range (1,11):
                print(f"{i} + {num} = {i+num}")
                
        elif op == 4:
            for i in range (1,11):
                print(f"{i} - {num} = {i-num}")
                
        else:
            print("opção inválida...")
        
        break

    fim = input("Continuar? (s/n)").upper().strip()
else:
    print("\n\nO programa foi encerrado.")

"""Atividade 02:
Soma de Números de 1 a 100:
Crie um programa que use um laço for para somar
todos os números de 1 a 100 e exiba o resultado."""

print("- - - - -  - Soma de todos os números de 1 a 100 - - - - - -")
soma = 0
for i in range (1,101)
    soma += i
print(f"Total = {soma}")


"""Atividade 03:
Caractere por Caractere:
Escreva um programa que solicite uma palavra ao usuário e use um
laço for para exibir cada caractere da palavra em uma linha separada."""

print("----- palavra fragmentada -----")
texto = input("\nDigite uma palavra ou texto: ")
for i in texto:
    print(i)
    
"""Atividade 04:
Contagem Regressiva de 10 a 1:
Desenvolva um programa que use um laço for para fazer uma
contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!"."""

print("----- Contagem regressiva -----")
for i in range(10,0,-1):
    print(i)
else:
    print("Feliz ano novo! 🎉🥳")

"""Atividade 05:
Contagem de Números Positivos e Negativos:
Escreva um programa que solicite ao usuário 10 números e use um
laço for com uma condicional para contar quantos são positivos e
quantos são negativos."""

print("-----Números positivos e negativos-----")
print("Digite 10 números:")
pos = 0
neg = 0
zero = 0
for i in range(0,10):
    print(f"{i+1}) ")
    num = int(input())
    if num > 0:
        pos += 1
    elif num < 0:
        pos += 1
    else:
        zero += 1

print("Contagem:")
print(f"Positivo: {pos}\nNegativo: {neg}")
if zero > 0:
    print(f"Zero: {zero}")

"""Atividade 06:
Soma de Números Pares:
Escreva um programa que use um laço for para somar
todos os números pares de 1 a 50 e exiba o resultado final."""
print("----- SOMA DOS PARES DE 1 A 50 -----")
soma = 0
for i in range (1,51):
    if i%2 == 0:
        soma += i

print(f"Total: {i}")

"""Atividade 07:
Contagem de Vogais em uma Palavra:
Crie um programa que solicite uma palavra ao usuário e use um laço for com
uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém."""

vogais = "AEIOUÁÉÍÓÚÀÈÌÒÙÄËÏÖÜÂÊÎÔÛÃÕÆ"
texto = input("Insira uma palavra ou texto: ").upper().strip()
vogal = 0

for letra in texto:
    if letra in vogais:
        vogal += 1
print(f"{texto} tem {vogal} vogais")


"""Atividade 08:
Cálculo de Média de Notas:
Escreva um programa que solicite 5 notas de alunos. Use um laço for
para somar as notas e uma condicional para exibir a média e a
classificação ("Aprovado" para média >= 6,
"Reprovado" para média < 6)."""
provas = 5
nota = 0
soma = 0
for i in range (provas):
    print(f"Prova {i+1}")
    nota = float(input("Digite a da prova: "))
    soma += nota

media = soma/provas
print(f"A media do aluno é: {media}")
if (media >= 6):
    print("APROVADO!!! 🥳🎉")
else:
    print("REPROVADO... ❌")

"""Atividade 09:
Verificar Números Pares e Impares com Interrupção:
Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para
identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break."""

"""Atividade 10:
Contar Números Positivos e Negativos:
Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos
são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break."""
    
"""Atividade 11:
Verificar Múltiplos de 5 e Parar:
Escreva um programa que use um laço for para imprimir números de 1 a 30.
Use uma condicional para verificar se um número é múltiplo de 5 e outro
para verificar se é maior que 20 e interromper o loop com break.
"""

"""Atividade 12:
Soma de Números com Desconto:
Peça ao usuário para inserir 5 preços de produtos. Use um laço for para
calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e
interrompa o loop com break."""