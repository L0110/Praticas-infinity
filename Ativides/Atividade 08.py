"""Escreva um programa que solicite 5 notas de alunos. Use um laço for
para somar as notas e uma condicional para exibir a média e a
classificação ("Aprovado" para média >= 6,
"Reprovado" para média < 6)."""

print("*** *** Calculo de media de notas *** ***\n\n\n\n")
soma = 0
provas = 5
for i in range(provas):
    nota = float(input(f"Insira a nota da prova {i+1}: "))
    soma += nota
else: 
    media = soma/provas
    print(f"A media do aluno e: {media}")
    if media >= 6:
        print("O aluno esta APROVADO 🎉")
    else:
        print("O aluno esta REPROVADO ❌")
