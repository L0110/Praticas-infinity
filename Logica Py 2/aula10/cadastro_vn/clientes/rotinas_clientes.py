import flet as ft
from base_dados.dados import (clientes, )

# Salva os dados do cliente e atualiza a interface:
def salvar_cliente(pagina: ft.Page, codigo, nome, telefone):
    from geral import (gera_codigo, )

    dict_cliente = {
        'codigo': int(codigo.value),
        'nome': nome.value.upper(),
        'telefone': telefone.value
    }
    clientes.append( dict_cliente ) 

    # Atualiza o código e limpa os campos
    codigo.value = gera_codigo(clientes)
    nome.value = None
    telefone.value = None

    # Renderiza as alterações
    pagina.update()


# Funções para criar a página de Clientes (View):
def pagina_clientes(pagina):
    from geral import (gera_codigo, voltar)
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
