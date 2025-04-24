"""
Propor aos participantes que criem um aplicativo de lista de tarefas simples utilizando Flet.
Incluir funcionalidades como adicionar, remover e marcar tarefas como concluídas.
Incentivar a utilização de eventos e interações do usuário.

"" - ADICIONAR
"" - REMOVER
"" - MARCAR COMO CONCLUÍDA
"""

import flet as ft

class Task(ft.Row):
    def __init__(self, text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, visible=False)
        self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(
            visible=False, icon=ft.icons.SAVE, on_click=self.save
        )
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
        ]

    def edit(self, e):
        self.edit_button.visible = False
        self.save_button.visible = True
        self.text_view.visible = False
        self.text_edit.visible = True
        self.update()

    def save(self, e):
        self.edit_button.visible = True
        self.save_button.visible = False
        self.text_view.visible = True
        self.text_edit.visible = False
        self.text_view.value = self.text_edit.value
        self.update()

def main(janela: ft.Page):
    janela.title = "Lista de tarefas v0.01"
    janela.bgcolor = ft.colors.AMBER

    titulo = ft.Text(
        value="Lista de tarefas",
        size=32,
        color=ft.colors.AMBER,
        bgcolor=ft.colors.WHITE,
    )

    campoInserir = ft.TextField(
        label="Nova tarefa",
        hover_color=ft.colors.RED,
        border_color=ft.colors.WHITE,
        fill_color=ft.colors.WHITE,
        focused_border_color=ft.colors.RED,
        color=ft.colors.AMBER,
        label_style=ft.TextStyle(
            color=ft.colors.WHITE,
        ),
        max_length=90,
    )

    campoLista = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
        padding=10,
    )

    def f_incluir(e):
        if campoInserir.value.strip():
            nova_tarefa = Task(campoInserir.value)
            campoLista.controls.append(nova_tarefa)
            campoLista.update()
            campoInserir.value = ""
            campoInserir.update()
        else:
            print("O campo de texto está vazio!")

    incluir = ft.ElevatedButton(
        text="Salvar ",
        data="botão",
        on_click=f_incluir,
        icon=ft.icons.ADD,
    )

    def f_remover(e):
        if campoLista.controls:
            campoLista.controls.pop()
            campoLista.update()
        else:
            print("Nenhuma tarefa para remover!")

    remover = ft.ElevatedButton(
        text="Remover ",
        data="botão",
        on_click=f_remover,
        icon=ft.icons.DELETE,
    )

    janela.controls = [titulo, campoInserir, incluir, campoLista, remover]
    janela.add(
        ft.Row(controls=[campoInserir, incluir]),
        campoLista,
        ft.Row(controls=[remover]),
    )

ft.app(main)