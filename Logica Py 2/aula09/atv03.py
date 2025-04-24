"""
O aplicativo deve ser capaz de realizar operações básicas de matemática, como adição, subtração, multiplicação e divisão.
Implemente uma interface limpa e intuitiva, com botões para os números e operações, além de uma área para exibir o resultado das operações.
"""

import flet as ft

def principal(janela:ft.Page):
    janela.title = "Calculadora v0.01"
    janela.bgcolor = ft.colors.BLUE_200

    janela.update()
ft.app(principal)
    