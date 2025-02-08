import flet as ft

def pagina_produtos(pagina):
    from geral import (voltar, )
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