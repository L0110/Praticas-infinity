'''1- Conversão de Unidades:
Crie um programa que converta metros para centímetros.
Peça ao usuário para digitar um valor em metros, armazene
em uma variável e converta para centímetros. '''
print("Conversor: Metros para Centímetros")
m = float(input("\n\nInsira a madida em Metros: "))

print(f"{m} metros equivale a {m*100} centímetros")

'''2- Cálculo de Área:
Crie um programa que calcule a área de um retângulo.
Peça ao usuário para digitar a largura e a altura,
armazene em variáveis e calcule a área.
'''

print("Cálculo de área do retângulo")
m1=float(input("Insira o valor do lado 01"))
m2=float(input("Insira o valor do lado 02"))
print(f"Área: {m1*m2}")

'''3- Cálculo de IMC:
Crie um programa que calcule o Índice de Massa Corporal (IMC).
Peça ao usuário para digitar seu peso e altura, armazene em
variáveis e calcule o IMC.'''
print("Cálculo de IMC")
peso = float(input("Insira o peso em Kg: "))
alt = float(input("Insira a altura em metros: "))
imc = peso/(alt**2)
print(f"IMC: {imc}")

'''4- Cálculo de Juros Simples:
Crie um programa que calcule o valor futuro de um investimento
usando a fórmula de juros simples. Peça ao usuário para digitar o
capital inicial, a taxa de juros e o tempo de aplicação.'''
print("Cálculo de Juros Simples")
c= float(input("Capital a investir: R$ "))#capital
i= float(input("Porcentagem da taxa de jutos '%': "))/100#taxa
t= float(input("Tempo da aplicação 'Meses': "))#tempo
j=c*i*t
print(f"Aplicação com rendimentopor {t} meses: {j}")


'''5- Algoritmo de Cálculo de Desconto:
Crie um algoritmo que peça quatro notas de um aluno, calcule a
média e exiba se o aluno foi aprovado ou reprovado (média >= 6).'''
print("Algoritmo de Cálculo de média")
print("Notas do aluno :")

a=float(input("Insira a nota da prova 1: "))
b=float(input("Insira a nota da prova 2: "))
c=float(input("Insira a nota da prova 3: "))
d=float(input("Insira a nota da prova 4: "))

media = (a+b+c+d)/4
if media >= 6:
    print(f"Aluno aprovado!\n média= {media}")
else:
    print(f"Aluno REPROVADO.\n média= {media}")
    
'''6- Algoritmo de Cálculo de Desconto:
Desenvolva um algoritmo que calcule o preço de um produto
após aplicar um desconto. Solicite o preço original e o percentual
de desconto.'''

print("Cálculo de Desconto")
vlr = float(input("Valor do produto: R$"))
desc = float(input("Desconto "'%'":"))/100
calc = vlr-(vlr*desc)
print(f"Valor R$ {vlr}")
print(f"Desconto aplicado: R$ {desc}")
print(f"Toral R$ {calc}")

'''7- Algoritmo de Conversão de Tempo:
Desenvolva um algoritmo que converta uma quantidade de
segundos fornecida pelo usuário em horas, minutos e segundos.'''
print("Algoritmo de Conversão de Tempo")
s = float(input("Segundos: "))
tmp = s
h= 0
m= 0
if s>=60:
    m = s/60
    s = s%60
    if m>=60:
        h = m/60
        m = m%60

print(f"{tmp} segundos equivale a:")
print(f"Tempo {int(h)}:{int(m)}:{int(s)}")

'''8- Algoritmo de Conversão de Temperatura:
Crie um algoritmo que converta uma temperatura de Celsius
para Fahrenheit. Solicite ao usuário a temperatura em Celsius
e exiba o resultado em Fahrenheit.'''
print("Algoritmo de Conversão de Temperatura")
c = float(input("Temperatura em Celsius: "))
f = (c * 1.8) + 32
print(f"{c} C°  equivale a {f} F°")

'''9- Categoria de Idade:
Desenvolva um programa que peça a idade do usuário e
informe se ele é criança, adolescente, adulto ou idoso.'''
print("Categoria de Idade")
idade = int(input("Idade: "))
if idade<12:
    print("Criança")
elif idade<18:
    print("Adolescente")
elif idade<60:
    print("Adulto")
else:
    print("Idoso")

'''10- Classificação de Notas:
Crie um programa que solicite uma nota de 0 a 100
e informe o conceito (A, B, C, D, F) com base na nota.'''

nota = -1
while (nota <0) or (nota>100):
    nota = int(input("Informe NOTA: "))
    if nota >= 90:
        print("Conceito A")
    elif nota >= 80:
        print("Conceito B")
    elif nota >= 70:
        print("Conceito C")
    elif nota >= 60:
        print("Conceito D")
    else:
        print("Conceito F")

'''11- Verificar Signo:
Escreva um programa que peça o dia e o mês de
nascimento do usuário e informe o signo correspondente.'''

print("Verificar Signo")
dia = int(input("Dia de Nascimento: "))
mes = int(input("Mês de Nascimento: "))
if (mes == 3 and dia >= 21) or (mes == 4 and dia  <= 20):
    print("Áries")
if (mes == 4 and dia >= 21) or (mes == 5 and dia  <= 20):
    print("Touro")
if (mes == 5 and dia >= 21) or (mes == 6 and dia  <= 20):
    print("Gemeos")
if (mes == 6 and dia >= 21) or (mes == 7 and dia  <= 22):
    print("Cancer")
if (mes == 7 and dia >= 23) or (mes == 8 and dia  <= 22):
    print("Leão")
if (mes == 8 and dia >= 21) or (mes == 9 and dia  <= 22):
    print("Virgem")
if (mes == 9 and dia >= 23) or (mes == 10 and dia  <= 22):
    print("Libra")
if (mes == 10 and dia >= 23) or (mes == 11 and dia  <= 21):
    print("Escorpião")
if (mes == 11 and dia >= 22) or (mes == 12 and dia  <= 21):
    print("Sargitário")
if (mes == 12 and dia >= 22) or (mes == 1 and dia  <= 20):
    print("Capricórnio")
if (mes == 1 and dia >= 21) or (mes == 2 and dia  <= 18):
    print("Aquário")
if (mes == 2 and dia >= 19) or (mes == 3 and dia  <= 20):
    print("Peixes")

'''12- Sistema de Login:
Desenvolva um programa que simule um sistema de login.
O programa deve pedir o nome de usuário e a senha e verificar
se correspondem a um usuário pré-cadastrado. Exiba mensagens
apropriadas para login bem-sucedido ou falha.'''
print("Sistema de Login")

log = False
while log == False:
    nome = input("Usuario: ").upper().strip()
    senha = input("Senha: ")
    if nome == "ZE" and senha == "123456":
        log = True
        print("Login Bem-sucedido!")
        break
    else:
        print("Login Falho!")

'''13- Contagem Regressiva:
Desenvolva um programa que use um laço while para exibir uma
contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".'''
print("Contagem Regressiva")
contagem = 10
while contagem > 0:
    print(contagem)
    contagem -= 1
else:
    print("Feliz Ano Novo!")



'''14- Contagem Regressiva:
Desenvolva um programa que use um laço for para exibir uma
contagem regressiva de 10 até 1 e, em seguida, exiba "Feliz Ano Novo!".'''
print("Contagem Regressiva")
contagem = 10
for i in range (contagem,0,-1):
    print(contagem)
else:
    print("Feliz Ano Novo!")

'''15- Soma de Números Pares:
Crie um programa que use um laço while para somar
todos os números pares de 1 a 100 e exiba o resultado.'''
contador = 1
soma = 0
while contador <= 100:
    soma += contador
    contador  += 1
print(f"Soma = {soma}")

'''16- Tabuada de um Número:
Faça um programa que solicite um número ao usuário e use
um laço for para exibir a tabuada desse número (de 1 a 10).'''
print("Tabuada de multilicação de um número")
numero = int(input("Digite um número: "))
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")

'''17- Verificação de Palíndromo:
Escreva um programa que solicite uma palavra ao usuário e
use um laço while para verificar se a palavra é um palíndromo
(lê-se da mesma forma de trás para frente).'''
palavra = input("Digite uma palavra: ").upper().strip()
cont = 0
while cont < len(palavra):
    if palavra[cont] == palavra[-(cont+1)]:
        cont += 1
    else:
        break
    if cont == len(palavra):
        print(f"A palavra '{palavra}' é um palíndromo.")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")

'''18-Sistema de Login com Tentativas Limitadas:
Desenvolva um programa que simule um sistema de login.
O programa deve solicitar o nome de usuário e senha até que o
usuário insira as credenciais corretas ou até que o número máximo
de tentativas seja atingido. Use um laço while com uma condicional
para verificar as credenciais e limitar as tentativas.'''
print("Sistema de Login")
tentativas = 0
while tentativas < 3:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if usuario == "admin" and senha == "1234":
        print("Login realizado com sucesso!")
        break
    else:
        tentativas += 1
        print(f"Tentativas restantes: {3 - tentativas}")
else:
    print("Número máximo de tentativas atingido. Login negado!")
