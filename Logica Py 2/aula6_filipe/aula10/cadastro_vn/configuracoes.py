import flet as ft

def pagina_configuracoes(pagina: ft.Page):
    from geral import ( voltar, )
    from tkinter import ( Tk, )

    largura_monitor_usuario = Tk().winfo_screenwidth()
    largura_max_pagina = largura_monitor_usuario
    altura_max_pagina = pagina.height
    '''
    print("Largura Inicial: ", largura_max_pagina)
    print("Largura Inicial: ", pagina.window.width)
    print("Largura Tela usuário: ", largura_monitor_usuario)

    print("Altura Inicial: ", altura_max_pagina)
    print("Altura Inicial: ", pagina.window.height)
    '''
    
    def alterar_tema(e):
        pagina.theme_mode = "light" if tema_dropdown.value == "Claro" else "dark"
        #pagina.theme = ft.Theme(color_scheme_seed="brown") if tema_dropdown.value == "Claro" else ft.Theme(color_scheme_seed="blue")
        pagina.update()

    
    def alterar_dimensoes(e):
        pagina.window.left=0
        pagina.window.width = int( largura_max_pagina * float(largura_slider.value ) )
        print(pagina.window.width)
        pagina.window.height = int( altura_max_pagina * float(altura_slider.value ) )
        print( pagina.window.height )
        pagina.update()
    

    
    tema_dropdown = ft.Dropdown(
        label="Tema",
        options=[
            ft.dropdown.Option("Claro"),
            ft.dropdown.Option("Escuro"),
        ],
        value="Claro",
        on_change=alterar_tema,
    )

    notificacoes_checkbox = ft.Checkbox(
        label="Ativar notificações",
        value=True,
    )

    modo_desenho_switch = ft.CupertinoSwitch(
        label="Modo Desenho",
        value=False,
    )

    largura_slider = ft.CupertinoSlider(
        on_change=alterar_dimensoes,
        value=1,
    )

    altura_slider = ft.CupertinoSlider(
        on_change=alterar_dimensoes,
        value=1,
    )
    print("*** config ***")
    return ft.View(
        route="/configuracoes",
        controls=[
            ft.Text("Configurações do Sistema", style="headlineMedium"),
            ft.Text("Tema", style="titleMedium"),
            tema_dropdown,
            ft.Divider(),
            ft.Text("Notificações", style="titleMedium"),
            notificacoes_checkbox,
            ft.Divider(),
            ft.Text("Modo Desenho", style="titleMedium"),
            modo_desenho_switch,
            ft.Divider(),
            ft.Text("Dimensões da Página", style="titleMedium"),
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Largura"),
                            largura_slider,
                        ]
                    ),
                    ft.Column(
                        [
                            ft.Text("Altura"),
                            altura_slider,
                        ]
                    ),
                ]
            ),
            ft.Divider(),
            ft.ElevatedButton("Salvar Configurações", on_click=lambda e: salvar_configuracoes(
                tema_dropdown.value,
                notificacoes_checkbox.value,
                modo_desenho_switch.value,
                largura_slider.value,
                altura_slider.value
            )),
            ft.ElevatedButton("Voltar", on_click=lambda e: voltar(pagina)),
        ],
        #bgcolor=ft.colors.GREY_100,
    )

def salvar_configuracoes(tema, notificacoes, modo_desenho, largura, altura):
    print(f"Tema: {tema}")
    print(f"Notificações Ativadas: {notificacoes}")
    print(f"Modo Desenho Ativo: {modo_desenho}")
    print(f"Largura da Página: {largura}px")
    print(f"Altura da Página: {altura}px")
    # Aqui você pode implementar lógica para salvar essas configurações no banco de dados ou arquivo.

