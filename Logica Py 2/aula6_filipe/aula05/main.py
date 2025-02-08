from func import soma
from func import med
from func import concatenar_strings


"""resultado = soma(5,3)
print(resultado)"""

print("--- CALCULO DE MÉDIA ---")
"""nota1 = float(input("Insira a nota da prova 1"))
nota2 = float(input("Insira a nota da prova 2"))
nota3 =float(input(f"Insira a nota da prova 3"))

print(f"A média das notas é {media(nota1,nota2,nota3)}")"""

soma = list
for i in range (3):
    nota = float(input(f"Insira a nota da prova {i+1}"))
    soma.append(nota)
    print(f"A média das notas é {med(soma)}")  #chamando a função med com a lista soma como argumento 
    soma.clear() #limpando a lista para que possa ser usada novamente


nome = input("insira o nome: ")
endereco = input("insira o endereco: ")
cpf = input("insira o cpf: ")
idade = input("insira a idade: ")


print("Lista de valores inseridos:")
print(concatenar_strings(nome, idade, cpf, endereco))