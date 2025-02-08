import flet as ft

clientes = {}


def gera_codigo(base_dados: dict):
    if len(base_dados)==0:
        return '1'
    else:
        return str( (tuple( base_dados.keys() )[-1]  + 1 ) )

# Salva os dados do cliente e atualiza a interface:
def salvar_cliente(pagina: ft.Page, codigo, nome, telefone):
    clientes[int(codigo.value)] = {
        "nome": nome.value,
        "telefone": telefone.value,
    }
    print(clientes)

    # Atualiza o código e limpa os campos
    codigo.value = gera_codigo(clientes)
    nome.value = None
    telefone.value = None

    # Renderiza as alterações
    pagina.update()

# Funções para criar as páginas
def pagina_clientes(pagina):
    codigo = ft.Text(gera_codigo(clientes), size=14, color=ft.colors.BROWN_400)
    nome = ft.TextField(label="Nome do Cliente", color=ft.colors.BROWN_600)
    telefone = ft.TextField(label="Telefone", color=ft.colors.BROWN_600)
    
    return ft.View(
        route="/clientes",
        controls=[
            ft.Text("Cadastro de Clientes", style="headlineMedium"),
            codigo,
            nome,
            telefone,
            ft.ElevatedButton("Salvar", on_click=lambda e: salvar_cliente( 
                pagina,
                codigo,
                nome,
                telefone 
            ) ),
            ft.ElevatedButton("Voltar", on_click=lambda e: voltar(pagina) ),
        ],
        bgcolor=ft.colors.BLUE_200,
    )

def pagina_produtos(pagina):
    return ft.View(
        route="/produtos",
        controls=[
            ft.Text("Cadastro de Produtos", style="headlineMedium"),
            ft.TextField(label="Nome do Produto"),
            ft.TextField(label="Preço"),
            ft.ElevatedButton("Salvar", on_click=lambda e: print("Produto salvo!")),
            ft.ElevatedButton("Voltar", on_click=lambda e: voltar(pagina) ),
        ],
        bgcolor=ft.colors.LIGHT_GREEN_200,
    )

# Página de Pedidos
def pagina_pedidos(pagina):
    return ft.View(
        route="/pedidos",
        controls=[
            ft.Text("Cadastro de Pedidos", style="headlineMedium"),
            ft.TextField(label="Número do Pedido"),
            ft.TextField(label="Cliente"),
            ft.ElevatedButton("Salvar", on_click=lambda e: print("Pedido salvo!")),
            ft.ElevatedButton("Voltar", on_click=lambda e: voltar(pagina) ),
        ],
        bgcolor=ft.colors.LIGHT_BLUE_ACCENT_700,
    )

# Relatório Geral de Produtos
def rel_geral_produtos(pagina):
    return ft.View(
        route="/rel_geral_produtos",
        controls=[
            ft.Text("Relatório Geral de Produtos", style="headlineMedium"),
            ft.ElevatedButton("Imprimir", icon=ft.icons.PRINT ,on_click=lambda e: voltar(pagina) ),
            ft.ElevatedButton("Voltar", on_click=lambda e: voltar(pagina) ),
        ],
        bgcolor=ft.colors.ORANGE_300,
    )

# Relatório Geral de Clientes:
def rel_geral_clientes(pagina):
    

    # Lista de Cards gerados dinamicamente com base nos dados do dicionário:
    cards_clientes = [
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.PERSON),
                            title=ft.Text(f"Nome: {cliente['nome']}"),
                            subtitle=ft.Text(f"Telefone: {cliente['telefone']}"),
                        ),
                        ft.Row(
                            controls=[
                                ft.TextButton("Editar"),
                                ft.TextButton("Excluir"),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
        for cliente in clientes.values()
    ]

    
    return ft.View(
        route="/rel_geral_clientes",
        controls=[
            ft.Text("Relatório Geral de Clientes", style="headlineMedium"),
            *cards_clientes,
            ft.ElevatedButton("Imprimir", icon=ft.icons.PRINT ,on_click=lambda e: voltar(pagina) ),
            ft.ElevatedButton("Voltar", on_click=lambda e: voltar(pagina) ),
        ],
        bgcolor=ft.colors.ORANGE_400,
    )

# Relatório Pedidos por Cliente:
def rel_pedidos_cliente(pagina):
    return ft.View(
        route="/rel_pedidos_cliente",
        controls=[
            ft.Text("Relatório Pedidos por Cliente", style="headlineMedium"),
            ft.TextField(hint_text="Código do Cliente"),
            ft.ElevatedButton("Imprimir", icon=ft.icons.PRINT ,on_click=lambda e: voltar(pagina) ),
            ft.ElevatedButton("Voltar", on_click=lambda e: voltar(pagina) ),
        ],
        bgcolor=ft.colors.ORANGE_500,
    )

# Função para navegar entre as páginas
def abrir_pagina(evento, pagina: ft.Page):
    # Obtendo a opção de MENU escolhida pelo usuário:
    opcao = evento.control.data

    if opcao == "sair":
        pagina.window.close()
        return None

    if opcao in rotas:
        nova_pagina = rotas[opcao](pagina)  # Chama a função correspondente
        pagina.views.append(nova_pagina)
        pagina.go(nova_pagina.route)

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



# -------------------+  Página principal  +-------------------------------
def principal(janela: ft.Page):
    # Configurações da página principal
    janela.title = "Cadastro de Produtos - v.1.0.0"
    janela.bgcolor = ft.colors.DEEP_PURPLE_ACCENT_700

    # MenuBar com opções
    menubar = ft.MenuBar(
        opacity=0.9,
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.center,
            bgcolor=ft.colors.ORANGE_900,
            shadow_color=ft.colors.AMBER_100,
        ), 
        controls=[
            funcao_cadastros(janela),
            funcao_relatorios(janela),
            ft.MenuItemButton(content=ft.Text("Sair"), data="sair", on_click=lambda e: abrir_pagina(e, janela)),
        ],
    )

    # Adiciona o MenuBar no topo da página
    janela.add(
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
            alignment=ft.MainAxisAlignment.CENTER
        ),
    )

# Mapeamento de rotas para funções de criação de páginas
rotas = {
    "clientes": pagina_clientes,
    "produtos": pagina_produtos,
    "pedidos": pagina_pedidos,
    "rel_geral_clientes": rel_geral_clientes,
    "rel_geral_produtos": rel_geral_produtos,
    "rel_pedidos_cliente": rel_pedidos_cliente,
}

# Inicializa a aplicação
ft.app(target=principal)
