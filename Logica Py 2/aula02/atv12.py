"""
Crie um programa que simule um sistema de votação. O
programa deve permitir que os eleitores escolham entre
opções de eleitores e conte os votos para cada opção.
Use um dicionário para armazenar os resultados da

votação, onde as chaves são as opções e os valores são o
número de votos para cada opção. O programa deve
permitir que os eleitores votem, encerre a votação e exiba
os resultados finais. Use While True e pare o programa
somente se o usuário digitar o número 0 e exiba os resultados finais.
"""
import os

def limpar_tela(): 
    if os.name == 'nt': 
        os.system('cls') 
    else: os.system('clear')

print("#"*60)
print("Votação")
print("#"*60)

candidatos={1:"Zé",
           2:"José",
           3:"Cleitim",
           4:"Zéia",
           5:"Samara"}

contador={}

for l in range(11,0,-1):
    print(f"Eleitores restantes: {l-1}")

    print("Boca de urna:")

    for k,v in candidatos.items():
        print(f"Número: {k}, Candidato: {v}")
    try:
        voto = int(input("Número do seu candidato: "))

        if voto in candidatos:
            if voto in contador:
                contador[voto]+=1
            else:
                contador[voto]=1
        else:
            if voto not in contador:
                contador["nulo"] = 1
            else:
                contador["nulo"] += 1

    except ValueError:
        print("Por favor, insira um valor")

print("####################################")

for k,v in contador.items():
    print(f"Número: {k}, Candidato:{v}")
print("####################################")
        