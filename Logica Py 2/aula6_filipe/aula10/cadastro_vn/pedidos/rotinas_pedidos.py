import flet as ft

# Página de Pedidos
def pagina_pedidos(pagina):
    
    from geral import (voltar, )

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
