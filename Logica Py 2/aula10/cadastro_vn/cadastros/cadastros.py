import flet as ft
from geral import (funcao_cadastros, funcao_relatorios, abrir_pagina)

# -------------------+  Página principal  +-------------------------------
def principal(janela: ft.Page):


    def mew(e):
        if e.data == 'close':
            janela.open(confirmacao)
    
    # Configurações da página principal
    janela.title = "Cadastro de Produtos - v.1.0.0"
    janela.window.center()
    #janela.bgcolor = ft.colors.DEEP_PURPLE_ACCENT_700
    #janela.window.prevent_close = True
    #janela.window.on_event = mew
    # Verificando a rota ATUAL:
    janela.on_route_change = lambda e: print("Rota atual: ", janela.route )
    
    
    confirmacao = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to exit this app?"),
        actions=[
            ft.ElevatedButton("Yes", on_click=janela.window.destroy() ),
            ft.OutlinedButton("No", on_click=lambda: janela.close(confirmacao) ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

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
            #funcao_cadastros(janela),
            #funcao_relatorios(janela),
            ft.MenuItemButton(content=ft.Text("Configurações"), data="configuracoes", on_click=lambda e: abrir_pagina(e, janela)),
            ft.MenuItemButton(content=ft.Text("Sair"), data="sair", on_click=lambda e: abrir_pagina(e, janela)),
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
ft.app(target=principal)
