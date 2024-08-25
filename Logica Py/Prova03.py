"""
Você está criando um programa em Python para simular um jogo simples de adivinhação. 
O programa deve gerar um número aleatório entre 1 e 10 e pedir ao jogador para adivinhar o número. 
O jogador terá até 3 tentativas para acertar.

Implemente o jogo utilizando um loop 'while' para permitir que o jogador faça múltiplas tentativas até acertar 
ou atingir o limite de tentativas. Utilize a estrutura 'else' para exibir uma mensagem de encorajamento caso o 
jogador acerte e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.
"""
import random
tentativa = 3
aleatorio = random.randint(1,10)

print("######   ADIVINHE O NUMERO   ######")

while tentativa > 0:
    print(f"\n\nChances: {tentativa}")
    num = int(input("Digite um numero entre 1 e 10: "))
    if(num != aleatorio) and (tentativa == 3):
        print("Tente mais uma vez\n\n")
        tentativa -= 1
    elif(num != aleatorio) and (tentativa == 2):
        print("Voce consegue, tente mais uma vez!\n\n")
        tentativa -= 1
    elif(num != aleatorio) and (tentativa == 1):
        print("Mais uma chance. Você chegou perto... talvez\n\n")
        tentativa -= 1
    else:
        print(f"Muito bem!🎉 o numero secreto é: {aleatorio}")
        break

print(f"Você não tem mais chances. \n\nO numero secreto era: {aleatorio}")
print("O programa será encerrado.")
