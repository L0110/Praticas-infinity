"""Crie uma tupla para representar as informações de três palestrantes,
cada uma contendo o NOME, TEMA DA PALESTRA e a INSTITUIÇÃO a qual estão vinculadas.

Exiba na tela as informações do terceiro palestrante. incluindo NOME, TEMA da palestra e INSTITUIÇÃO 
"""

palestrante = ("Davi Olufemi", "Pedro Henrique","João Miguel")
tema = ("Inglês de NY","Segurança civil","Didática, lógica e programação")
instituicao = ("CCAA Shopping Conquista Sul","15ª Delegacia","Campus Party")

p = list(palestrante)
t = list(tema)
i = list(instituicao)

print("Palesrante: ", p[2],end="\n")
print("Tema: ", t[2],end="\n")
print("Instituição: ", i[2],end="\n")