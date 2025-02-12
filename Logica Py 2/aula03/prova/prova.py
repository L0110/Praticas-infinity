"""
Crie um dicionário para armazenar o nome e o preço de cinco produtos. 
Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como 
o valor associado a essa chave. Após a inserção de todos os produtos e preços, calcule o valor total da compra somando 
todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra.
"""
catalogo = {}

print("+"*60)
print("Cadasro de produtos")
print("+"*60)
fim = ""

while fim != "N":
    produtos = input("insira o nome do produto: ")
    valor = float(input("Valor do produto: R$ "))
    catalogo[produtos] = valor
    
    while fim != "N" or fim != "S":
        fim = input("Deseja adicionar mais produtos? (S/N)").upper().strip()
        if fim == "N" or fim == "S":
            break
        else:
            print("Opcao invalida")
#---------------------------------------------------------------------

print("-"*60)
print("Catalogo")
print("-"*60)
soma = 0
for item in catalogo:
    print(f"{item} - R$ {catalogo[item]}")
    soma += catalogo[item]
#---------------------------------------------------------------------
    
print("="*60)
print(f"Total: R$ {soma}")