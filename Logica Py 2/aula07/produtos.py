from funcoes import (gera_codigo, colunas,limpar_tela,pausa)
from banco_dados.dados import(produtos, )

# 04 - listagem
def listagem_geral_produtos():
    print("~" * colunas)
    print(f"CÓDIGO \tNOME\t\t\tPREÇO\tQUANTIDADE")
    for produto in produtos:
        print(f"   {produto['codigo']}\t{produto['nome']}\t\t{produto['preco']}\t   {produto['quantidade']}")
    
    print("~" * colunas)



def listagem_simples_produtos():
    print("~" * colunas)
    for produto in produtos:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}")
    
    print("~" * colunas)



#Buscar código
def busca_codigo(codigo):
    lista_codigos = [p["codigo"]for p in produtos]
    if not codigo in lista_codigos:
        return -1
    else:
        indice = lista_codigos.index(codigo)
        return indice




# 01 - Cadastro
def incluir_produtos():
    print("+" * colunas)
    print("Incluir Produtos")
    print("+" * colunas)
    while True:
        codigo = gera_codigo(produtos)
        nome = input("Digite o nome do produto: ").strip().upper()
        preco = float(input("Digite o preço do produto: ").strip())
        qt = int(input("Informe a quantidade do produto: ").strip())
        dict_dados = {"codigo": codigo, "nome": nome, "preco": preco, "quantidade": qt}
        """print(dict_dados)"""
        produtos.append(dict_dados)
        """print(produtos)"""
        
        listagem_geral_produtos()
        continuar = input("Deseja incluir mais produtos? (S/N): ").strip().upper()
        if continuar != "S":
            break
        

# 02 - Alterar        
def alterar_produtos():
    print("-" * colunas)
    print("Alterar Produtos")
    print("-" * colunas)

    while True:
        listagem_geral_produtos()
        codigo = int(input("informe o código do produto a alterar:"))
        indice = busca_codigo(codigo)
        if indice < 0:
            print("Produto não cadastrado.")
        else:
            print("+" * colunas)
            info = int(input("Informe: [1]-Nome, [2]-Preço, [3]-Quantidade:"))
            print(f"CÓDIGO \tNOME\t\t\tPREÇO\tQUANTIDADE")
            print(f"   {produtos[indice]['codigo']}\t{produtos[indice]['nome']}\t\t{produtos[indice]['preco']}\t   {produtos[indice]['quantidade']}")

        #Alterar nome do produto:
            if info == 1:
                print(f"Nome atual: {produtos[indice]['nome']}")
                nome = input("Digite o NOVO nome do produto: ").strip().upper()
                produtos[indice]['nome'] = nome
                print(f"Nome do produto alterado para {nome}")
            elif info == 2:
                print(f"Preço atual: R$ {produtos[indice]['preco']}")
                novo_preco = float(input(f"Infoirme o NOVO PREÇO do produto: ").strip())
                produtos[indice]['preco'] = novo_preco
                print(f"Preço do produto alterado para R$ {novo_preco}")
            elif info == 3:
                print(f"Quantidade atual: {produtos[indice]['quantidade']}")
                nova_qt = int(input("Infoirme a NOVA QUANTIDADE do produto: ").strip())
                produtos[indice]['quantidade'] = nova_qt
                print(f"Quantidade do produto alterada para {nova_qt}")
            else:
                print("Opção inválida.")
            
            #listagem_geral_produtos()
            continuar = input("Deseja alterar mais produtos? (S/N): ").strip()
            if continuar != "S":
                break



# 03 - Excluir
def excluir_produtos():
    print("-" * colunas)
    print("Excluir Produtos")
    print("-" * colunas)
    
    listagem_simples_produtos()

    print("x" * colunas)
    print("Exlusão de produtos")
    codigo = int (input("Digite o código do produto para excluir: ").strip())
    indice = busca_codigo(codigo)

    if indice < 0:
        print("Código não encontrado")
    else:
        confirma = input(f"tem certeza que quer excluir o produto {produtos[indice]['nome']}? (s/n): ").strip().upper()
        if confirma == "S":
            del produtos[indice]
            print("Produto excluido com sucesso")
        else:
            print("Exclusão cancelada")
            pausa()

    listagem_simples_produtos()
    pausa()
    limpar_tela()


def listagem_produto_especifico():
    codigo = int(input("Digite o código do produto que deseja buscar: "))
    indice = busca_codigo(codigo)
    print('.'*colunas)
    if indice < 0:
        print("Código não encontrado")

    total_geral = 0
    subtotal = 0
    for i,p in enumerate(produtos):
        subtotal = p['preco']*p['quantidade']
        if i== indice:
            sub_total = subtotal
        
        total_geral += subtotal