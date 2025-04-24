"""
Propor aos participantes que criem um formulário de cadastro utilizando Flet.
Incluir campos como nome, sobrenome, email, etc. Encorajar a aplicação de diferentes widgets e layouts
para organizar o formulário.
"""

import flet

"""def main(page: flet.Page):
    ola = flet.Text(value="Olá mundo!",size = 30)
    page.controls.append(ola)
    page.update()

flet.app(target=main)"""

def principal(janela:flet.Page):
    janela.title = "Minha App v0.02"
    janela.bgcolor = flet.colors.BLUE_200

    
    ola = flet.Text(
        value="Login super seguro e nada suseito para seu banco",
        size = 32,
        color= flet.Colors.BLUE_300,
        bgcolor=flet.Colors.LIGHT_GREEN_50
    )
    
    site = flet.TextField(
        prefix_text="www.",
        suffix_text=".com.br",
        max_length=10,
        label="Digite o Site",
        #value="teste",
        color=flet.Colors.BLACK38,
        #prefix_icons = flet.icons.SAVE,
        #suffix_icons = flet.icons.PRINT
    )

    login = flet.TextField(
        prefix_text="L:",
        label="Email ou CPF",
        color=flet.Colors.BLACK38,
        prefix_icon=flet.icons.MAN,
        data="Login",
        on_click=lambda e: print("Você clicou no login"),
        on_change=lambda e: print(e.data))
    senha = flet.TextField(
        prefix_text="*:",
        label="Digite sua senha",
        color=flet.Colors.BLACK38,
        password=True,
        prefix_icon=flet.icons.LOCK,
        data="Senha",
        on_click=lambda e: print("Você clicou na senha"),
        on_change=lambda e: print(e.data)
        )
        

    def f_salvar(e):
        print(login.value)
        print(senha.value)
        print("Evento: ", e.control.data)
        print("Evento: ", e.name)

    #salvar = flet.ElevatedButton(text = "Salvar",on_click = lambda e: print("Salvando..."),icon=flet.icons.SAVE)
    salvar = flet.ElevatedButton(text = "Salvar",
        data="botão",
        on_click = lambda e: f_salvar(e), 
        icon = flet.icons.SAVE,
        on_hover = lambda e: f_salvar(e))
    
    #print(site.value)
    janela.add(
        ola,login,senha,site,salvar
        #flet.Row(controls=[site,salvar])
    )
    janela.update()
flet.app(principal)