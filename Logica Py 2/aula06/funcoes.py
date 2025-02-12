#Interno
CONSTANTE = 60

import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')  # clear -> Linux/Mac cls -> Windows

def pausar():
    print("x" * int(CONSTANTE / 2))
    input("Pressione enter para continuar\n")
    limpar_tela()

lista_t = []
lt = lista_t

# Dicionarios principais
menu = {1: "nTarefa()",
        2: "nCategoria()",
        3: "listar()",
        4: "marcar()",
        5: "alterar_prioridade()",
        6: "excategoria()",
        7: "lista_cp()",
        8: "sair()"
        }

tarefa = {}

categoria = ["trabalho",
             "lazer",
             "viagem",
             "estudos",
             "compras"
             ]
categorias_disponiveis = [cat.lower() for cat in categoria]

prioridades = ['Alta', 'Média', 'Baixa']

teste_concluido = lambda concluido: "Concluída" if concluido else "Pendente"


# Menu

#01
def criar_tarefa():
    nova_tarefa = {}
    nova_tarefa['nome'] = input("Nome da tarefa: ")
    nova_tarefa['descricao'] = input("Descrição: ")
    categorias_disponiveis = [categoria.lower() for categoria in categoria]
    print(categorias_disponiveis)
    nova_tarefa['categoria'] = input("Nome da categoria: ").lower().strip()
    while nova_tarefa['categoria'] not in categorias_disponiveis:
        print(f"A categoria '{nova_tarefa['categoria']}' não está listada. Deseja adicioná-la? (s/n)")
        resposta = input().lower().strip()
        if resposta == 's':
            categoria.append(nova_tarefa['categoria'])
        else:
            print("Categoria inválida. Tente novamente.")
        nova_tarefa['categoria'] = input("Nome da categoria: ").lower().strip()
    
    # Escolher prioridade
    print("Escolha a prioridade da tarefa: Alta, Média, Baixa")
    nova_tarefa['prioridade'] = input("Prioridade: ").capitalize().strip()
    while nova_tarefa['prioridade'] not in prioridades:
        print("Prioridade inválida. Escolha entre: Alta, Média, Baixa")
        nova_tarefa['prioridade'] = input("Prioridade: ").capitalize().strip()
    
    nova_tarefa['concluido'] = False
    return nova_tarefa

def nTarefa():
    print("+" * CONSTANTE)
    print("Inclusão de tarefas: ")
    nova_tarefa = criar_tarefa()
    lista_t.append(nova_tarefa)
    pausar()
    return

#02
def nCategoria():
    print("+" * CONSTANTE)
    print("Inclusão de categorias: ")
    novo = input("Nome da categoria: ").lower().strip()
    print(f"{novo} adicionada.")
    categoria.append(novo)
    pausar()
    return

#03
def agrupar_por_prioridade(tarefas):
    prioridades_agrupadas = {'Alta': [], 'Média': [], 'Baixa': []}
    for tarefa in tarefas:
        prioridade = tarefa['prioridade']
        if prioridade in prioridades_agrupadas:
            prioridades_agrupadas[prioridade].append(tarefa)
    return prioridades_agrupadas

def listar():
    print("-" * CONSTANTE)
    print("Lista de tarefas por prioridade")
    print("-" * CONSTANTE)
    print("=" * CONSTANTE)
    tarefas_agrupadas = agrupar_por_prioridade(lista_t)
    
    for prioridade, tarefas in tarefas_agrupadas.items():
        print(f"Prioridade: {prioridade}")
        for tf in tarefas:
            print(f"  {tf['nome']} - {tf['descricao']} - {tf['categoria']} - {teste_concluido(tf['concluido'])}")
        print("=" * CONSTANTE)

    pausar()
    return

def listar():
    print("-" * CONSTANTE)
    print("Lista de tarefas por categoria")
    print("-" * CONSTANTE)
    print("=" * CONSTANTE)

    tarefas_agrupadas = agrupar_por_categoria(lista_t)
    
    for categoria, tarefas in tarefas_agrupadas.items():
        print(f"Categoria: {categoria.capitalize()}")
        for tf in tarefas:
            print(f"  {tf['prioridade']} - {tf['nome']} - {tf['descricao']} - {teste_concluido(tf['concluido'])}")
        print("=" * CONSTANTE)

    pausar()
    return
#04
def teste_concluido(concluido):
    return "Concluído" if concluido else "Em aberto"

def marcar():
    print("*" * CONSTANTE)
    print("Tarefas em aberto")
    tarefas_abertas = list(filter(lambda tarefa: tarefa['concluido'] == False, lista_t))

    if not tarefas_abertas:
        print("Não há tarefas em aberto.")
    else:
        for i, tf in enumerate(tarefas_abertas):
            print(f"{i + 1}. {tf['prioridade']} - {tf['nome']} - {tf['descricao']} - {tf['categoria']} - {teste_concluido(tf['concluido'])}")

        print("\nEscolha o número da tarefa que deseja marcar como concluída:")
        escolha = int(input().strip()) - 1
        if 0 <= escolha < len(tarefas_abertas):
            tarefa_selecionada = tarefas_abertas[escolha]
            tarefa_selecionada['concluido'] = True
            print(f"Tarefa '{tarefa_selecionada['nome']}' marcada como concluída.")
        else:
            print("Escolha inválida.")

    print("*" * CONSTANTE)
    print("=" * CONSTANTE)

    pausar()
    return

#05
def alterar_prioridade():
    print("v" * CONSTANTE)
    print("Alterar prioridade de uma tarefa") 
    print("=" * CONSTANTE) 
    for i, tf in enumerate(lista_t): 
        print(f"{i + 1}. {tf['prioridade']} - {tf['nome']} - {tf['descricao']} - {tf['categoria']} - {teste_concluido(tf['concluido'])}") 
    
    print("\nEscolha o número da tarefa que deseja alterar a prioridade:") 
    escolha = int(input().strip()) - 1 
    if 0 <= escolha < len(lista_t): 
        print("Escolha a nova prioridade: Alta, Média, Baixa")
        nova_prioridade = input("Nova prioridade: ").capitalize().strip()
        while nova_prioridade not in prioridades:
            print("Prioridade inválida. Escolha entre: Alta, Média, Baixa")
            nova_prioridade = input("Nova prioridade: ").capitalize().strip()
        lista_t[escolha]['prioridade'] = nova_prioridade 
        print(f"Prioridade da tarefa '{lista_t[escolha]['nome']}' alterada para {nova_prioridade}.") 
    else: 
        print("Escolha inválida.") 

    pausar() 
    print("v" * CONSTANTE)
    print("=" * CONSTANTE)

    pausar()
    return

#06
def agrupar_por_categoria(tarefas):
    tarefas_agrupadas = {}
    for tarefa in tarefas:
        categoria = tarefa['categoria']
        if categoria not in tarefas_agrupadas:
            tarefas_agrupadas[categoria] = []
        tarefas_agrupadas[categoria].append(tarefa)
    return tarefas_agrupadas

def listar_categoria():
    print("-" * CONSTANTE)
    print("Lista de tarefas por categoria")
    print("-" * CONSTANTE)
    print("=" * CONSTANTE)

    tarefas_agrupadas = agrupar_por_categoria(lista_t)
    
    for categoria, tarefas in tarefas_agrupadas.items():
        print(f"Categoria: {categoria.capitalize()}")
        for tf in tarefas:
            print(f"  {tf['prioridade']} - {tf['nome']} - {tf['descricao']} - {teste_concluido(tf['concluido'])}")
        print("=" * CONSTANTE)

    pausar()
    return

#07
def lista_cp():
    print("*" * CONSTANTE)
    print("Tarefas Concluídas")
    tarefas_concluidas = list(filter(lambda tarefa: tarefa['concluido'] == True, lista_t))

    if not tarefas_concluidas:
        print("Não há tarefas concluídas.")
    else:
        for i, tf in enumerate(tarefas_concluidas):
            print(f"{i + 1}. {tf['prioridade']} - {tf['nome']} - {tf['descricao']} - {tf['categoria']} - {teste_concluido(tf['concluido'])}")

    print("-" * CONSTANTE)

    print("Tarefas em aberto")
    tarefas_abertas = list(filter(lambda tarefa: tarefa['concluido'] == False, lista_t))

    if not tarefas_abertas:
        print("Não há tarefas em aberto.")
    else:
        for i, tf in enumerate(tarefas_abertas):
            print(f"{i + 1}. {tf['prioridade']} - {tf['nome']} - {tf['descricao']} - {tf['categoria']} - {teste_concluido(tf['concluido'])}")

    print("*" * CONSTANTE)
    pausar()
    return

#08
def sair():
    print(">" * CONSTANTE)
    print("O programa foi encerrado.")
    print(">" * CONSTANTE)
    pausar()
    exit()
    return