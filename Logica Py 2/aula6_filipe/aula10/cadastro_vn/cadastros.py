import flet as ft
from geral import (funcao_cadastros, funcao_relatorios, abrir_pagina, confirmar_saida )

"""
    Esta aplicação de exemplo, trabalha com:

    a) Views: Múltiplas visões, se aproveitando do recurso de roteamento dessa classe.
    b) Objeto MenuBar e suas agregadas (SubmenuButton e MenuItemButton).
    
"""

# -------------------+  Página principal  +-------------------------------
def principal(janela: ft.Page):
    
    
    # Configurações da página principal
    janela.title = "Cadastro de Produtos - v.1.0.0"
    janela.window.center()
    #janela.bgcolor = ft.colors.DEEP_PURPLE_ACCENT_700
    janela.bgcolor = "#8B8000"
    janela.window.prevent_close = True
    janela.window.on_event = lambda e:confirmar_saida(e, janela)
    # Verificando a rota ATUAL:
    janela.on_route_change = lambda e: print("Rota atual: ", janela.route )
        
    # MenuBar com opções
    menubar = ft.MenuBar(
        opacity=0.9,
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.center,
            #bgcolor=ft.colors.ORANGE_900,
            #shadow_color=ft.colors.AMBER_100,
        ), 
        controls=[
            funcao_cadastros( janela ),
            funcao_relatorios( janela ),
            ft.MenuItemButton(
                content=ft.Text("Configurações"), 
                data="configuracoes", 
                on_click=lambda e: abrir_pagina(e, janela)
            ),
            ft.MenuItemButton( 
                content=ft.Text("Sair"), 
                data="sair", 
                on_click=lambda e: confirmar_saida(e, janela)
            ),
        ],
    )

    # Adiciona o MenuBar no topo da página
    janela.views.clear()
    janela.views.append(
        ft.View(
            route='/',   
            controls=[
                ft.Row(
                    controls=[menubar],  # MenuBar diretamente no topo
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            "Bem-vindo ao Sistema! Use o menu para navegar.", 
                            expand=True,
                            text_align=ft.TextAlign.CENTER,
                            size=32,
                            weight=900
                        ),
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
        ),
    )
    janela.update()

# Inicializa a aplicação
ft.app( principal )
