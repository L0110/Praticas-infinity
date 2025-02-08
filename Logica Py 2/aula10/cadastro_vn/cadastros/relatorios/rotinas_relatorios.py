import flet as ft
from base_dados.dados import (clientes, )

# Relatório Geral de Produtos
def rel_geral_produtos(pagina):
    from geral import (voltar, )
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
    

    from geral import (voltar, )
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
        for cliente in clientes
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
    from geral import (voltar, )
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
