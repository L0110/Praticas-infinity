#Interno
CONSTANTE = 60

def limpar_tela():
    import os
    os.system('clear') #clear -> Linux/Mac cls -> Windows

def pausar():
    print("x"*int(CONSTANTE/2))
    pause = input("Pressione enter para continuar\n")
    limpar_tela()

lista_t = {}
lt = lista_t

def contador():
    if not hasattr(contador,'x'):
        contador.x=0
    contador.x=1
    return contador.x
    



#Dicionarios principais
menu = {1:"nTarefa()",
        2:"nCategoria()",
        3:"listar()",
        4:"marcar()",
        5:"exprioridade()",
        6:"excategoria()",
        7:"lista_cp()",
        8:"sair()"
        }

for dic in lista_t:
    print(f"{contador} - {gic["nome"]}")

categoria = {1: "Trabalho",
             2: "Lazer",
             3: "Viagem",
             4: "Estudos",
             5: "Compras"
             }


#Menu

#01
def nTarefa():
    print("+"*CONSTANTE)
    print("Inclusão de tarefas: ")
    lt["nome"] = input("Nome da tarefa: ")
    lt["descricao"] = input("Descrição: ")
    print(categoria.values())
    lt["categoria"] = input("Nome da tarefa: ")
    lt["prioridade"] = contador()
    lt["concluido"] = False
    pausar()
    return
#02
def nCategoria():
    print("+"*CONSTANTE)
    print("Inclusão de categorias: ")
    
    
    pausar()
    return
#03
def listar():
    print("-"*CONSTANTE)
    print("Lista de tarefas")
    print("-"*CONSTANTE)
    print("="*CONSTANTE)


    pausar()
    return

#04
def marcar():
    print("*"*CONSTANTE)
    print("Tarefas em aberto")
    print("*"*CONSTANTE)
    print("="*CONSTANTE)

    pausar()
    return

#05
def exprioridade():
    print("v"*CONSTANTE)
    print("Tarefas em aberto")
    print("v"*CONSTANTE)
    print("="*CONSTANTE)

    pausar()
    return

#06
def excategoria():
    print("*"*CONSTANTE)
    print("Tarefas em aberto")
    print("*"*CONSTANTE)
    print("="*CONSTANTE)

    pausar()
    return

#07
def lista_cp():
    print("*"*CONSTANTE)
    print("Tarefas em Concluidas")
    print("-"*CONSTANTE)
    print("Tarefas em aberto")
    print("*"*CONSTANTE)
    pausar()
    return

#08
def sair():
    print(">"*CONSTANTE)
    print("O programa foi encerrado.")
    print(">"*CONSTANTE)
    pausar()
    exit()
    return  