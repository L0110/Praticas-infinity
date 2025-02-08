#import aula04Funcao as af
#from  aula04Funcao import saudacao as sau

#from  aula04Funcao import (saudacao1,saudacao2,saudacao3 )
from  aula04Funcao import * 
#usando o '*', são importadas todas as funções da biblioteca

#Chamadas da função

"""print("Saudação 1")
print(saudacao1())

print("Saudação 2")
user = input("Nome do usuário: ")
print(saudacao2(user))

print("Saudação 3")
print(saudacao3('Cabral'))

print("Saudação 4 com valor de entrada")
print(saudacao4('Caio'))
print("Saudação 4 sem valor de entrada")
print(saudacao4())

print("Saudação 5")
print(saudacao5("adélio", 'uma boa noite'))

print("Saudação 6(1)")
print(saudacao6(nome='',turno='um bom dia'))

print("Saudação 6(2)")
print(saudacao6(nome='João',turno='um bom dia'))

print("Saudação 6(3)")
print(saudacao6('João','um bom dia'))
"""

for f in range(5):
    nome = f"saudacao{f+1}()"
    print(eval(nome))

print(eval("1+2"))
print("1+2")

print(eval('saudacao3("João"),1+2'),1+2)

meuDicionario = {
    1:'saudacao1()',
    2:'saudacao2()'
}

menu = {
    1:'inlcuir()',
    2:'alterar()',
    3:'excluir()',
    4:'relatorio1()',
    5:'relatorio2()',
    6:'relatorio3()',
    7:'relatorio4()',
    8:'relatorio5()'
}

opcao = int(input(''))
eval(menu[opcao])