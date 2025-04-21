"""
Propor aos participantes que criem um aplicativo de lista de tarefas simples utilizando Flet.
Incluir funcionalidades como adicionar, remover e marcar tarefas como concluídas.
Incentivar a utilização de eventos e interações do usuário.
"""

import flet as ft

def main(janela:ft.Page):
    janela.title = "Lista de tarefas v0.01"
    janela.bgcolor = ft.colors.AMBER
    
    titulo = ft.Text(
        value = "Lista de tarefas",
        size= 32,
        color= ft.Colors.AMBER,
        bgcolor=ft.Colors.WHITE    
    )
    
    campoInserir = ft.TextField(
        label="Nova tarefa",
        hover_color= ft.colors.WHITE,
        border_color= ft.Colors.WHITE,
        fill_color= ft.Colors.AMBER,
        
        
        color= ft.Colors.AMBER,
        label_style=ft.TextStyle(
            color=ft.colors.WHITE,
            ),
        
        max_length=90,
    )
    
    def f_incluir(e):
        print(campoInserir.value)
        print("Evento: ", e.control.data)
        print("Evento: ", e.name)
    
    
    incluir = ft.ElevatedButton(text = "Salvar ",
        data="botão",
        on_click = lambda e: f_incluir(e), 
        icon = ft.icons.ADD,
    )
    
    
    janela.add(
        titulo,campoInserir,incluir
    )
    
ft.app(main)