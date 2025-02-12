"""
Crie um dicionário que relacione nomes de alunos às suas
notas em uma disciplina. Calcule a média das notas e exiba-a.    
"""

alunos = {1:"Zezinho",
          2:"Luizinho",
          3:"Huguinho",
          4:"Petralhina",
          5:"Kryptosson",
          6:"Maria Doge"}

notas = {1:[4.4,6.5,8.0,10.0],
         2:[6.4,7.0,8.6,10.0],
         3:[4.2,6.6,5.4,7.0],
         4:[6.5,10.0,10.0,10.0],
         5:[8,7,10.0,9.5,8.0],
         6:[8.0,8.0,8.0,8.0]}

media = []

for nota in notas:
    media.append(round(sum(notas[nota])/len(notas[nota]),2))

avAluno = {valor: alunos.get(None,chave) for chave, valor in zip(media,alunos.values())}

print(media)
print(avAluno)

