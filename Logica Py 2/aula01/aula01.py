nomes = ['ana','Zerca', 'maria', 'zaria' ,'joao', 'pedro', 'marcos']
print(nomes)
#Alterar ou substituir
nomes[1] = 'Zeca'

#Excluir
#Forma 01: del nomes[0]
backup = nomes.pop(0)
#Forma 03:  nomes.remove('ana')
#Forma 04:  nomes.clear()
#Forma 05:  nomes = []
#forma 06: nomes.pop(0)
print("Nomes: ",nomes)
print("Backup: ",backup)
exit()

lista1 = []
lista2 = list()

dados = ["12345", "jose Antonio", 12300,45]
for indice,valor in enumerate(dados):
#    lista1.insert(indice,valor.upper())
    if isinstance(valor, str):
        dados[indice] = valor.upper()
print(dados)
exit()

lista1.append(input("Digite algo: ").upper)
print("Lista1: ",lista1 )

exit()

nomes = ['ana', 'maria', 'zaria' ,'joao', 'pedro', 'marcos']
print("Nome especifico: ",nomes[0])
print("Nomes selecionados:", nomes[4:6])
print("Nomes selecionados2:", nomes[1:6:2])
for i in range (3):
    print("For: ",nomes[i])
for i in nomes:
    print("For2: ",i)
for indice,i in enumerate(nomes):
    print("Indice:", indice, "Nome: ",i)

novo_nome = input("Digite um novo nome a inserir na lista: ")
#insrerir  o novo nome na lista
nomes.append(novo_nome)
nomes.insert(1,'AROLDO')

print("Lista atualizada: ",nomes)
("Lista atualizada: ",nomes)
print(len(nomes))#imprime  o tamanho da lista

#print("Nome removido: ",nomes.pop(0))


#for i in range(3):
#    lista1.append(i)
#print(lista1)

exit()

nomes = ['ana', 'maria', 'zaria' ,'joao', 'pedro', 'marcos',]
copiaNomes = nomes.copy() #copia  a lista sem copiar o endereço da variavel original

copiaNomes.sort(reverse=True) #sort(reverse=True) imrime na ordem decrescente
print("antes: ",nomes)
print("depois",copiaNomes)

exit()

listaLetra = ['a','e',"i",'o','u']
print(listaLetra)

exit()

listaNum= [8,7,1,2,6,9,3,4,5]
print(f"{listaNum}")
listaNum.sort() #Organiza valores na ordem crescente
print(f"{listaNum}")

exit()

listaNum= [1,2,3,4,5]
print(f"{listaNum}")

exit()

for num in range(2,1101):
    for i  in range(2,num):
        if (num % i) == 0:
            print(f"O número {num} não é PRIMO")
            break
    else:
        print(f"{num} é um número primo")

exit()

#comando continue: enquanto a condição for verdadeira,  
# o programa continua executando o bloco de código acima dele, até que a condição que responde ao continue se torne falsa e permita o código avançar
for i in range(1,11):
    if i%2 !=0:
        print(f"impar => {i}. Pulando")
        continue
    print(f"par => {i}", end='')
exit()


total = 0

while True:
    preco = float(input("Digite o preço do produto ou [0] ara terminar: "))
    total += preco
    if preco == 0: break #Se o comando ocupar apenas uma linha, pode ser aplicado junto a linha do teste

#:.2f arredonda  o valor para duas casas decimais
print(f"R$ {total:.2f} a pagar")

exit()

#RANGE(MARCO INICIAL, MARCO FINAL,  PASSO)
for x in range(-90,100,2):
    print(x, end=' ')

exit()