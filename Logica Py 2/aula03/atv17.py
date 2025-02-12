#REVISÃO
import os as c
c.system('clear')

#17
meu_dic = {
    'nome': 'João',
    'idade': 20,
    'cidade': 'São Paulo',
    'status': True,
    'mensalidade': 99.99
    #'pagamentos:' pago(), #É possivel inserir funções
    }
print(meu_dic['nome'])
print(meu_dic['idade'])
print(meu_dic['mensalidade'])
print(meu_dic)

for chave in meu_dic:
    print(chave)
print()

for valor in meu_dic.values():
    print(valor)
print()

for chave, valor in meu_dic.items():
    print(chave,":",valor)
print() 

print("Existe idade?: ",'idade'in meu_dic)
print("Existe idade 22 anos?: ",20 in meu_dic.values())
print("Nome: ", meu_dic.get('nome'))
print(dict.fromkeys(meu_dic))
