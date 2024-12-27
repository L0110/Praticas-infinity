"""
Suponha que você está gerenciando uma competição esportiva e tem
uma lista de tuplas representando os resultados das equipes em
diferentes modalidades. Cada tupla contém o nome da equipe, seguido
por uma lista de pontuações obtidas em cada rodada da competição.

1.Calcule a média das pontuações de cada equipe e armazene esses
valores em uma nova lista chamada medias.
2.Ordene a lista medias em ordem decrescente.
3.Crie uma nova lista chamada classificacao que contém tuplas, onde
cada tupla contém o nome da equipe e sua média de pontuações.
4.Exiba na tela a classificação final das equipes, mostrando o nome da
equipe e sua média, da equipe com a pontuação mais alta para a
mais baixa.
"""

equipes = [
    ("Equipe A", [1.0, 2.0, 3.0, 4.0, 5.0]),
    ("Equipe B", [6.0, 7.0, 8.0, 9.0, 10.0]),
    ("Equipe C", [11.0, 12.0, 13.0, 14.0, 15.0]),
    ("Equipe D", [16.0, 17.0, 18.0, 19.0, 20.0])
]

#01__________________________________________________________________________
medias = []
for equipe in equipes:
    media = sum(equipe[1])/len(equipe[1])
    medias.append(media)

print(medias)

#02__________________________________________________________________________
medias_ordenadas = sorted(medias,reverse=True)
print(medias_ordenadas)

#03__________________________________________________________________________
classificacao = []
for equipe in equipes:
        classificacao.append((equipe[0], sum(equipe[1])/len(equipe[1]), equipe[1]))

ranking = sorted(classificacao, key=lambda x: x[1], reverse=True)


print("x"*60)
print("Classificacao")
print("x"*60)
i = 1

#04__________________________________________________________________________

for rank in ranking:
      print(f"Posição {i}: {rank[0]}. Classificação: {rank[1]}, pontuações: {sorted(rank[2], reverse=True)}")
      i += 1