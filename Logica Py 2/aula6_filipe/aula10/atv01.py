import flet as ft

def principal(janela: ft.Page):

    janela.title = "Estillização Básica"
    janela.bgcolors = "blue"
    janela.window.left=100

    #variaveis em objeto
    titulo = ft.Text(
        value = "Texto com cor personalizada",
        color = ft.colors.BLUE_800,
        bgcolor= ft.colors.YELLOW_300,
        size = 32,
        text_align= ft.TextAlign.CENTER,
        weight= ft.FontWeight.BOLD,

    )

    senha = ft.TextField(
        value = "",
        label = "Senha",
        prefix_icon= ft.icons.PASSWORD,
        password = True,
        bgcolor= ft.colors.LIGHT_BLUE,
    )


    #variaveis em memória
    janela.update()
    janela.add(
        ft.Container(
            border_radius=10,
            bgcolor = "pink",
            content = ft.Row(
                controls = [
                    titulo,
                    ft.ElevatedButton(
                        bgcolor = "green",
                        text= "Botão com estilo",
                        color = 'white',
                        on_click= lambda e:print("Botão 'Com estilo' pressionado"),
                    ),
                    
                ] 
            ),
        ),senha 
        
    )
        

    #manipulação de objeto
    titulo.bgcolor = "red"

ft.app(target = principal)