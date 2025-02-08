from funcoes import (colunas, limpar_tela)
from produtos import *

while True:
    print("=" * colunas)
    print("1 - Cadastrar")
    print("2 - Alteração de produtos")
    print("3 - Exclusão de produtos")
    print("4 - Listagem geral produtos")
    print("." * colunas)
    print("5 - Sair")
    print("=" * colunas)

    opcao = input(': ').strip().upper()
    limpar_tela()


    match(opcao):
        case '1':
            incluir_produtos()
        case '2':
            alterar_produtos()
        case '3':
            excluir_produtos()
        case '4':
            print("~" * colunas)
            print("Produtos Cadastrados:")
            listagem_geral_produtos()
        case '5':
            import time
            import sys
            print("Retorne em breve!",end="")
            for i in range(5):
                print(".",end="")
                sys.stdout.flush()
                time.sleep(1)
            exit()