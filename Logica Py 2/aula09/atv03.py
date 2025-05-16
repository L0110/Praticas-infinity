import flet as ft

def principal(janela: ft.Page):
    janela.title = "Calculadora v0.01"
    janela.bgcolor = ft.colors.BLUE_200

    janela.controls = [
        ft.Row(
            controls=[ft.Text(value="0", size=40)],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="1", on_click=lambda e: print("1")),
                ft.ElevatedButton(text="2", on_click=lambda e: print("2")),
                ft.ElevatedButton(text="3", on_click=lambda e: print("3")),
                ft.ElevatedButton(text="4", on_click=lambda e: print("4")),
                ft.ElevatedButton(text="5", on_click=lambda e: print("5")),
                ft.ElevatedButton(text="6", on_click=lambda e: print("6")),
                ft.ElevatedButton(text="7", on_click=lambda e: print("7")),
                ft.ElevatedButton(text="8", on_click=lambda e: print("8")),
                ft.ElevatedButton(text="9", on_click=lambda e: print("9")),
                ft.ElevatedButton(text="0", on_click=lambda e: print("0")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="+", on_click=lambda e: print("+")),
                ft.ElevatedButton(text="-", on_click=lambda e: print("-")),
                ft.ElevatedButton(text="*", on_click=lambda e: print("*")),
                ft.ElevatedButton(text="/", on_click=lambda e: print("/")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    ]

    janela.update()

ft.app(target=principal)