#REVISÃO
import random as r
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

exit()
#16
meu_set = ["Calça","Short","Camisa","Short"]
print(meu_set)
print(list(set(meu_set)))


exit()

#15
deposito = ["Calça","Short","Camisa","Short"]
print(deposito)
produto = input("Qual item deseja excluir?: ").strip().title()
backup = deposito.pop(deposito.index(produto))
print("Depois: ",deposito)
print("Backup: ",backup)
print("Quantidade de shorts: ", deposito.count("Short"))

exit()

#14
#criando uma lista
frutas = ("maçã","banana","laranja","abacaxi")

#metodo index():   retorna o indice da primeira ocorrencia do elemento especificado
indice_laranja = frutas.index("laranja")
print("ìndice da laranja:", indice_laranja) # Saída: 2

#metodo count():   retorna a quantidade de ocorrencias do elemento especificado
quantidade_bananas = frutas.coutn("banana")
print("quantidade de bananas:", quantidade_bananas) # Saída: 1

#Desenpacotando uma tupla
maca,banana,laranja,abacaxi = frutas
print("Fruta 1:", maca)
print("Fruta 2:", banana)
print("Fruta 3:", laranja)
print("Fruta 4:", abacaxi)


exit()
#13
minha_lista = [1,2,3,4,5] #lista mutavel
minha_lista[0] = 10 #modificação elemento
print("minha_lista") #saída [10,2,3,4,5]

minha_tupla = (1,2,3,4,5)
#minha_tula[0] = 10 #Isso  não funciona pois a tupla é imutável
print(minha_tupla)

exit()

#12
lista_grande = list(range(1,1_000_000))
print(lista_grande)


exit()

#11 - 01
estoque = ["calça","camisa","short","saia"]
print("Antes: ",estoque)
estoque.append("casaco")
print("Depois: ",estoque)
estoque.sort()
print("Depois do SORT: ",estoque)
estoque.sort(reverse = "True")
print("Depois do SORT REVERSE: ",estoque)
estoque.insert(3,"cinto")
print("Depois do INSERT",estoque)
estoque.remove("calça")
print("Depois do REMOVE",estoque)
print("\n\n")
estoque.append("parafuso")
print("ERRADO:",estoque)
backup = estoque.pop()
print("Depois do POP",estoque)
print("item  removido: ",backup)
print("\n\n")


exit()
#10
letras = ['a','b','c','d','e']
print(letras[-1])# letra 'e'
print(letras[-2])# letra 'd'
print(letras[-3])# letra 'c'
print(letras[-4])# letra 'b'
print(letras[-5])# letra 'a'

exit()
#09 - 02
for i in range(10):
    if  i % 2 == 1:
        continue
    print(i)

exit()


#09 - 01
for i in range(10):
    if  i % 2 == 0:
        continue
    print(i)

exit()

#08
for i in range(10):
    if i==5:
        break
    print(i)
exit()

#07
contador = 0
inicio = 0
fim = r.randint(1,99)
passo = r.randint(1,10)
for i in range(inicio,fim,passo):
    print(f"Indice = {contador} | Valor = {i}")
    contador += 1
exit()

#06 - 02
lista=["Calça","Camisa","Saia","Short","Meia"]
print(lista[0:2])
####################
print(tuple (filter(lambda roupa: len(roupa)<5, lista) ) )


exit()
#06 - 01

lista=[1,2,3,4,5]
for item in lista:
    print(item)

exit()

#05
for indice in range(0,11):
    print(indice)

exit()

#04
while True:
    print("Vou imprimir PRA SEMPRE MUAHAHAHAHAHA")

exit()

#03
subindo = 0
while True:
    subindo += 1
    print(f'Valor subindo... \nValor Atual - {subindo}')
    if subindo == 10:
        c.system('clear')
        print('Parando')
        break
exit()

#02
validacao = 0

while validacao <10:
    print(f"A variavel validação - {validacao} é menor que 10")
    validacao = validacao + 1

exit()

#01
idade = r.randint(0,99)

if idade < 17:
    print('Você é menor de idade.')
elif idade <=19 and idade>17:
    print('Você é maior de idade.')
else:
    print('Você tem mais de 19 anos!')
