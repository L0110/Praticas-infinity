from funcoes import *






while True:
    #EXIBIÇÃO MENU
    print("="*CONSTANTE)
    "tarefas, listar tarefas, marcar tarefas como concluídas, exibir tarefas por prioridade ou categoria,"
    print("1- Adicionar tarefas")
    print("2- Adicionar Categorias")
    print("3- Listar tarefas")
    print("4- Marcar tarefas como concluídas")
    print("5- Exibir tarefas por prioridade")
    print("6- Exibir tarefas por categoria")
    print("7- Exibir tarefas concluídas/pententes")
    print("."*60)
    print("8- Sair")
    print("="*60)

    op = int(input(": "))
    
    limpar_tela()
    
    if op in menu:
        eval(menu[op])
    else:
        print("Opção inválida!")
        


    