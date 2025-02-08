import flet as ft
import asyncio
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
    "configuracoes": pagina_configuracoes,
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
    
    
    def handle_menu_item_click():
        return False


    return ft.SubmenuButton(
        content=ft.Text("Cadastros"),
        expand=True,
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Clientes"),

                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Inclusão"), 
                        leading=ft.Icon(ft.icons.ADD), 
                        close_on_click=False, 
                        style=ft.ButtonStyle( bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200} ),
                        data='clientes_inclusao',
                        on_click=lambda e: abrir_pagina(e, pagina)
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Alteração"),
                        leading=ft.Icon(ft.icons.UPDATE),
                        close_on_click=False,
                        style=ft.ButtonStyle( bgcolor={ft.ControlState.HOVERED: ft.colors.PURPLE_200} ),
                        on_click=lambda e: abrir_pagina(e, pagina)
                    ),
                    ft.CupertinoFilledButton(
                        text="Exclusão",
                        expand=False,
                        border_radius=5,
                        icon="delete_forever",
                        on_click=lambda e: abrir_pagina(e, pagina)
                        
                    ),
                    ft.ElevatedButton(
                        text="Relatório 1",
                        icon=ft.icons.REPORT,
                        elevation=1,
                        expand=True,
                        icon_color=ft.colors.BLUE_100,
                        tooltip="Relatório Geral de Clientes",
                        style=ft.ButtonStyle(
                            overlay_color=ft.colors.PURPLE_200,
                            shadow_color=ft.colors.PURPLE_900,
                            shape=ft.RoundedRectangleBorder(radius=5),
                        ),
                        on_click=lambda e: handle_menu_item_click()
                    ),
                ],
            ),
            ft.MenuItemButton(content=ft.Text("Produtos"), data="produtos", on_click=lambda e: abrir_pagina(e, pagina) ),
            ft.MenuItemButton(content=ft.Text("Pedidos"), data="pedidos", on_click=lambda e: abrir_pagina(e, pagina) ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(icon=ft.icons.POWER_INPUT, text="Check power"),
                    ft.PopupMenuItem(
                        content=ft.Row(
                            [
                                ft.Icon(ft.icons.HOURGLASS_TOP_OUTLINED),
                                ft.Text("Item with a custom content"),
                            ]
                        ),
                        on_click=lambda _: print("Button with a custom content clicked!"),
                    ),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=lambda e: handle_menu_item_click()
                    ),
                ] 
            ),
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
def abrir_pagina(evento: ft.ControlEvent, pagina: ft.Page):
    # Obtendo a opção de MENU escolhida pelo usuário:
    opcao = evento.control.data
    
    if opcao in rotas:
        nova_pagina = rotas[opcao](pagina)  # Chama a função correspondente
        pagina.views.append(nova_pagina)
        pagina.go(nova_pagina.route)


def confirmar_saida(e, janela):
    def fechar():
        confirmacao.open = False
        fechar_app( janela )


    confirmacao = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirmação"),
        content=ft.Text("Você quer SAIR da Aplicação?"),
        actions=[
            ft.ElevatedButton("Sim", on_click= lambda e: fechar() ),
            ft.OutlinedButton("Não", on_click=lambda e: janela.close(confirmacao) ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    if (e.control.data=='sair') or (e.data=='close'): 
        janela.open( confirmacao )


def fechar_app(pagina: ft.Page):    
    # Adiciona os elementos visuais
    progress_bar = ft.ProgressBar(
        width=pagina.window.width,
        color= ft.colors.AMBER_500,
        bgcolor=ft.colors.BLACK,
        visible=True
    )
    
    progress_ring = ft.ProgressRing(
        width=16, 
        height=16, 
        stroke_width = 3
    )
    
    pagina.overlay.append( progress_bar )
    '''
    pagina.overlay.append( 
        ft.Row( 
            controls=[progress_ring, ft.Text(
                value="Terminando aplicação...",
                text_align=ft.TextAlign.CENTER
            ) ] ,
            alignment=ft.alignment.bottom_center,
            height=int( pagina.window.height * 0.8 ),
            width=int( pagina.window.width * 0.8 ),
        ) 
    )
    '''
    '''
    pagina.overlay.append( 
        ft.CupertinoActivityIndicator(
            radius=50,
            color=ft.colors.RED,
            animating=True,
        ) 
    )
    '''
    pagina.update()

    # Aguarda para exibir os elementos
    async def fechar_com_atraso():
        await asyncio.sleep(3)
        pagina.window.destroy()

    asyncio.run(fechar_com_atraso())