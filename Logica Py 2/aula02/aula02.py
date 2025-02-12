'''DICIONARIO = TABELA HASH'''
#3

def f():
    return f"Boa tarde!"

dic = {}
#CRUD =  CREATE, READ, UPDATE, DELETE
# Inclusão:
dic['nome'] = 'João'
dic['CPF']= '456.787.100.01'
dic['Idade']= 33
dic['STATUS']=True
dict['funcao']= f()
print(dic)
#Alteração
dic['nome'] = 'João Pedro'
print(dic)
#Exclusão
del dic['Idade']
print(dic)
#Leitura
print(dic['nome'])
print(dic['CPF'])
print(dic['STATUS'])
print(dic['funcao'])
print(dic.get('nome')) #retorna o valor do dicionário, se não encontrar retorna
print(dic.get('nome', 'Não encontrado')) #retorna o valor do dicionário,
#se não encontrar retorna o valor padrão
print(dic.get('nome', None)) #retorna o valor do dicionário,


exit()
#1
dicionario = {
    'instituicao':'Infinity School',
    'Curso':'Dev Full Stack',
    'Módulo':'Java'
}

dados = {
    1:"Infinity",
    2:"Sala",
    3:"Banana"
}
dados[3]="Maçã"
dicionario['Módulo']='Python'

#nDicionario = {}
nDicionario = dict()
nDicionario = dict([('Módulo','Python'),('Instituição','Infinity School')])
nDicionario2 = dict(Modulo = "Python", Instituicao = "Infinity School")
print(nDicionario)
print(nDicionario2)
#2
dicionario = {elemento: f'Valor {elemento}' for elemento in range(6)}
print(dicionario)

exit()


"""Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas, usando conjuntos."""
sorteados = ["Tonin", "Ariel", "Josielton","Frederickson"]
sorteadas = ["Gleide", "Katrina", "Neide", "Ariel" ]
sort = set(sorteados)
sort2 = set(sorteadas)
print( sort.union(sort2))


exit()

"""Crie um programa que recebe dois conjuntos e exibe a interseção deles."""
a = {"a", "b", "c"}
b = {"b", "c", "d"}
c = a.intersection(b)
print(c)

exit()
"""PESQUISE EXPRESSÕES REGULARES
-REGEX
"""
"""Crie dois conjuntos, A e B, e realize a união dos dois conjuntos."""
a={"aba"}
b={"cate"}
c = a.union(b)
print(c)

exit()

listaCompras = [
    [],['sabão','papel higiênico','pasta de dente'],['macarrão prego','macarrão instantãneo','massa de pastel']
]
categoria = int(input("Categoria: [1] - Higiêne pessoal, [2] - Massas: "))
produto = input("Insita o NOME do produto: ").strip().upper()
listaCompras[categoria-1].append(produto)
print(listaCompras)

exit()

"""Crie um conjunto chamado frutas_vermelhas e adicione as seguintes frutas a ele: "morango" ,"cereja" e "framboesa". Em seguida, imprima o conjunto."""
frutas_vermelhas = {'morango', 'cereja',  'framboesa'}
print(frutas_vermelhas)
"""Remova a fruta "cereja" do conjunto frutas_vermelhas e imprima o conjunto atualizado."""
frutas_vermelhas.discard()
print(frutas_vermelhas)


"""Peça a um chat gerar uma lista em python que crie uma lista com os nomes de 100 produtos comumentes achados em supermercados.
Elabore um programa com essa lista que verifica se um produto digitado  pelo usuário está na lista de produtos ou não"""
estoque = [
    "Arroz", "Feijão", "Açúcar", "Café", "Farinha de trigo", "Óleo de soja", "Leite", "Pão", 
    "Margarina", "Queijo", "Presunto", "Mortadela", "Carne bovina", "Frango", "Peixe", "Macarrão", 
    "Molho de tomate", "Sal", "Pimenta", "Maionese", "Mostarda", "Ketchup", "Manteiga", "Creme de leite", 
    "Leite condensado", "Biscoito", "Bolacha", "Achocolatado", "Suco de laranja", "Refrigerante", 
    "Água mineral", "Cerveja", "Vinho", "Vodka", "Arroz integral", "Lentilha", "Grão-de-bico", "Ervilha", 
    "Milho verde", "Sardinha em lata", "Atum em lata", "Peito de peru", "Bacon", "Linguiça", "Alface", 
    "Tomate", "Cebola", "Alho", "Cenoura", "Batata", "Abobrinha", "Berinjela", "Brócolis", "Couve", 
    "Espinafre", "Pepino", "Pimentão", "Manga", "Maçã", "Banana", "Laranja", "Limão", "Abacaxi", 
    "Mamão", "Melancia", "Melão", "Uva", "Morango", "Goiaba", "Iogurte", "Requeijão", "Leite fermentado", 
    "Queijo ralado", "Ovo", "Pão de forma", "Pão francês", "Torrada", "Massa fresca", "Pizza congelada", 
    "Lasanha congelada", "Nuggets", "Peixe congelado", "Vegetais congelados", "Sorvete", "Chocolate", 
    "Bala", "Chiclete", "Gelatina", "Iogurte grego", "Granola", "Cereal", "Barra de cereal", "Amendoim", 
    "Castanha", "Nozes", "Pistache", "Papel higiênico", "Sabão em pó", "Detergente", "Amaciante de roupas", 
    "Suco de uva", "Suco de maçã", "Suco de abacaxi", "Suco de goiaba", "Suco de maracujá", "Água de coco", 
    "Leite de coco", "Creme de leite fresco", "Nata", "Leite desnatado", "Leite integral", "Leite em pó", 
    "Iogurte natural", "Iogurte de morango", "Iogurte de baunilha", "Iogurte de pêssego", "Queijo mussarela", 
    "Queijo prato", "Queijo parmesão", "Queijo brie", "Queijo camembert", "Queijo cottage", "Queijo minas", 
    "Queijo coalho", "Linguiça calabresa", "Linguiça toscana", "Carne de porco", "Carne de cordeiro", 
    "Carne de vitela", "Hambúrguer", "Salsicha", "Frango desfiado", "Frango assado", "Peixe frito", 
    "Peixe grelhado", "Salmão", "Tilápia", "Atum fresco", "Camarão", "Lula", "Polvo", "Marisco", 
    "Caranguejo", "Lagosta", "Bacalhau", "Azeitona preta", "Azeitona verde", "Palmito", "Champignon", 
    "Alcaparras", "Mostarda Dijon", "Mostarda amarela", "Pepino em conserva", "Beterraba", "Rabanete", 
    "Chuchu", "Mandioca", "Inhame", "Cará", "Jiló", "Abóbora", "Chicória", "Rúcula", "Agrião", 
    "Repolho", "Couve-flor", "Nabo", "Batata-doce", "Batata baroa", "Pera", "Pêssego", "Ameixa", 
    "Kiwi", "Maracujá", "Caju", "Acerola", "Jabuticaba", "Pitanga", "Siriguela", "Tangerina", 
    "Jaca", "Caqui", "Frutas cristalizadas", "Frutas secas", "Ameixa seca", "Uva passa", "Damasco seco", 
    "Tâmara", "Figo seco", "Coco ralado", "Gergelim", "Linhaça", "Chia", "Goiabada", "Doce de leite", 
    "Pé de moleque", "Rapadura", "Biscoito de polvilho", "Biscoito de maisena", "Biscoito recheado", 
    "Bolacha Maria", "Bolacha cream cracker", "Bolacha água e sal"]

pesquisa = input("Digite um item para localizar no estoque: ").upper().strip()
print("Pesquisa: ", pesquisa)
if pesquisa in estoque:
    print("O item ",pesquisa,"Está disponível")
else:
    print("O item ",pesquisa,"Não está disponível")

exit()
"""
crie um conjunto vazio chamado frutas e adicione as
seguintes frutas a ele: "maçã" "banana , uva, laranja e morango. Em seguida, imprima o conjunto.
"""

cesta = []
cesta = list()
cesta.append("maçã")
cesta.append("banana")
cesta.append("uva")
cesta.append("laranja")
cesta.append("morango")
print(cesta)

"""Verifique se a fruta "banana" está presente no conjunto frutas e imprima o resultado."""

print("Pesquisa: Banana - " ,"banana" in cesta)

exit()

"""print({'*'+letra+'*' for letra in ['a','b',"c",'a'] if letra != 'b'})

exit()"""

entrada = {'Cleiton','Josana','Edileusa'}
for x in entrada:
    print(x)

print(entrada.remove("Josana"))#Remove o item da lista, mas ao ser acionado novamente, o programa é interromido com erro*try eccept - key error)
print(entrada.discard("Josana"))#Remove o item da lista, mas ao ser acionado novamente,  o programa não é interrompido com erro
print(entrada)
entrada2 =  {'Cleiton','Socorrido','Miriane'}
print('Interserção: ',entrada.intersection(entrada2))#Imprime apenas o dado em comumn entre os dois sets
print('União: ',entrada.union(entrada2))#Imprime todos os dados dos dois sets
exit()

lista =['pedrosoueu@hotmail.com','anamail@gmail.com','cheilacabeleireira@gmailcom','pedrosoueu@hotmail.com' ]
print(lista)
conjunto = set((lista))
print("Conjunto: ",conjunto) #set é uma coleção de elementos não ordenados e não indexados

lista = list(conjunto)
print("Lista: ",lista)

exit()


set1 = {'Infinity','School','2024'}
print(set1)

"""set2 = {letra for letra in ['abacate'] if letra not in 'aeiou'}
print(set2) #set2 = {'b','c','t'}
"""
set1.add('Full')
print(set1)

novo_set={'Stack'}
set1.update(novo_set)
print(set1)

convidados = {'Jão'}
print('Jão' in convidados)
print('Erliane' in convidados)

