"""
Crie um dicionário que relacione nomes de alunos às suas
notas em uma disciplina. Calcule a média das notas e exiba-a.    
"""

alunos = ["Zezinho","Luizinho","Huguinho","Petralhina","Kryptosson","Maria Doge"]

notas = {1:[4.4,6.5,8.0,10.0],
         2:[6.4,7.0,8.6,10.0],
         3:[4.2,6.6,5.4,7.0],
         4:[6.5,10.0,10.0,10.0],
         5:[8,7,10.0,9.5,8.0],
         6:[8.0,8.0,8.0,8.0]}
avaliacao = set()
media = set()

for aluno in alunos:
    avaliacao.add(alunos.index(aluno))

for nota in notas:
    media.add(sum(notas[nota])/len(notas[nota]))

print(avaliacao)
print(media)


