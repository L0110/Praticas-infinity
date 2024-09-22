"""Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. 
O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome 
e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.
Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou 
reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, 
média e a indicação de aprovação ou reprovação.
Ao final, exiba a média geral da turma."""

numero_alunos = int(input("Insira o número de alunos: "))
media_geral = 0

for i in range(numero_alunos):
    nome = input(f"Insira o nome do aluno {i+1}: ")
    nota1 = float(input("Insira a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))
    nota3 = float(input("Insira a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3
    media_geral += media

    if media >= 7.0:
        print(f"{nome}, Notas: {nota1}, {nota2}, {nota3}, Media: {media:.2f}, Aprovado")
    else:
        print(f"{nome}, Notas: {nota1}, {nota2}, {nota3}, Media: {media:.2f}, Reprovado")

print(f"\nMedia geral da turma: {media_geral / numero_alunos:.2f}")
