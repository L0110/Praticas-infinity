import flet as ft
#from navegacao import (rotas, )
from produtos.rotinas_produtos import ( pagina_produtos, )
from clientes.rotinas_clientes import ( pagina_clientes, )
from pedidos.rotinas_pedidos import ( pagina_pedidos, )
from configuracoes import ( pagina_configuracoes, )
from relatorios.rotinas_relatorios import *


# Mapeamento de rotas para funções de criação de páginas
rotas = {
    "clientes": pagina_clientes,
    "produtos": pagina_produtos,
    "pedidos": pagina_pedidos,
    "rel_geral_clientes": rel_geral_clientes,
    "rel_geral_produtos": rel_geral_produtos,
    "rel_pedidos_cliente": rel_pedidos_cliente,
    "configuracoes": pagina_configuracoes
}


def gera_codigo(base_dados: dict):
    if len(base_dados)==0:
        return '1'
    else:
        return str( base_dados[-1]['codigo']  + 1 ) 


# Função para voltar à página anterior
def voltar(pagina):
    
    if len(pagina.views) > 1:
        pagina.views.pop()
        pagina.go(pagina.views[-1].route)


# Função com os Widgets do Sub Menu de Cadastros:
def funcao_cadastros(pagina):
    return ft.SubmenuButton(
        content=ft.Text("Cadastros"),
        expand=True,
        controls=[
            ft.MenuItemButton(content=ft.Text("Clientes"), data="clientes", on_click=lambda e: abrir_pagina(e, pagina) ),
            ft.MenuItemButton(content=ft.Text("Produtos"), data="produtos", on_click=lambda e: abrir_pagina(e, pagina) ),
            ft.MenuItemButton(content=ft.Text("Pedidos"), data="pedidos", on_click=lambda e: abrir_pagina(e, pagina) ),
        ],
    )


# Função com os Widgets do Sub Menu de Relatórios:
def funcao_relatorios(pagina):
    return ft.SubmenuButton(
        content=ft.Text("Relatórios"),
        expand=True,
        controls=[
            ft.MenuItemButton(content=ft.Text("Relatório Geral de Clientes"), data="rel_geral_clientes", on_click=lambda  e: abrir_pagina(e, pagina) ),
            ft.MenuItemButton(content=ft.Text("Relatório Geral de Produtos"), data="rel_geral_produtos", on_click=lambda e: abrir_pagina(e, pagina) ),
            ft.MenuItemButton(content=ft.Text("Relatório Pedidos por Cliente"), data="rel_pedidos_cliente", on_click=lambda e: abrir_pagina(e, pagina) ),
        ],
    )

def funcao_relatorios(pagina):
    return ft.SubmenuButton(
        content=ft.Text("Relatórios"),
        expand=True,
        controls=[
            ft.MenuItemButton(content=ft.Text("Relatório Geral de Clientes"), data="rel_geral_clientes", on_click=lambda  e: abrir_pagina(e, pagina) ),
            ft.MenuItemButton(content=ft.Text("Relatório Geral de Produtos"), data="rel_geral_produtos", on_click=lambda e: abrir_pagina(e, pagina) ),
            ft.MenuItemButton(content=ft.Text("Relatório Pedidos por Cliente"), data="rel_pedidos_cliente", on_click=lambda e: abrir_pagina(e, pagina) ),
        ],
    )


# Função para navegar entre as páginas
def abrir_pagina(evento, pagina: ft.Page):
    # Obtendo a opção de MENU escolhida pelo usuário:
    opcao = evento.control.data
    
    print("Opção = ", opcao)

    confirmacao = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to exit this app?"),
        actions=[
            ft.ElevatedButton("Yes", on_click=pagina.window.destroy() ),
            ft.OutlinedButton("No", on_click=lambda: pagina.close(confirmacao) ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    if (opcao == "sair") or (opcao=='close'):
        pagina.open(confirmacao)

    if opcao in rotas:
        nova_pagina = rotas[opcao](pagina)  # Chama a função correspondente
        pagina.views.append(nova_pagina)
        pagina.go(nova_pagina.route)


