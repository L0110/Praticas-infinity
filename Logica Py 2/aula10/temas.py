import flet as ft

tema_atual = 0
temas = {
    0: "Padrão",
    1: "red",
    2: "green",
    3: "blue900",
    4: "yellow",
    5: "orange",
    6: "brown",
    7: "amber",
    8: "pink",
    9: "cyan",
    10: "purple",
    11: "indigo",
    12: "lime",
    13: "gray",
    14: "blueGray",
    15: "teal",
}
def principal(janela: ft.Page):
    def mudar_tema(evento):
        global tema_atual
        if tema_atual >=len(temas)-1:
            tema_atual = 0
        else:
            tema_atual += 1       
        janela.theme = ft.Theme(color_scheme_seed=temas[tema_atual])
        print(f"Tema: {tema_atual} - {temas[tema_atual].upper()}" )
        dd.value=temas[tema_atual].upper()
        texto_cor.value = temas[tema_atual].upper()
        janela.update()
        
    def dd_alterar(evento):
        global tema_atual
        texto_cor.value = dd.value
        tema_atual = [v.upper() for v in temas.values() ].index( dd.value) 
        janela.theme = ft.Theme(color_scheme_seed=temas[tema_atual])
        janela.update()
    
    janela.title = "Teste de Temas do Flet"
    texto_cor = ft.TextField(f"Tema Atual: Padrão" )
    dd= ft.Dropdown( width=200, options=[], on_change=dd_alterar )
    for cor in temas.values():
        dd.options.append( ft.dropdown.Option( cor.upper() ) )
    
    janela.add(
        texto_cor,
        ft.TextField("Digite aqui:"),
        dd,
        ft.ElevatedButton(f"Mudar Tema!", on_click=mudar_tema)
    )
    janela.update()
ft.app( principal )