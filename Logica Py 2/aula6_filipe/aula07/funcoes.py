import os
colunas = 60

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')  # clear -> Linux/Mac cls -> Windows

def gera_codigo(base_dados: list):
    if len(base_dados) == 0 or None:
        return 1
    else:
        return base_dados [-1]['codigo']+1
    
def pausa():
    input("Pressione Enter para continuar...")


