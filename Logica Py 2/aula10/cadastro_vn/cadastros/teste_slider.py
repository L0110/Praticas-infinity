import flet as ft

name = "CupertinoSlider example"

def principal( janela: ft.Page):
    eslider=ft.CupertinoSlider(value=0.5, min=0, max=1)
    def example():
        return ft.Column(
            controls=[
                ft.Text("Cupertino slider:"),
                eslider,
                ft.Text("Material slider:"),
                ft.Slider(),
                ft.Text("Adaptive slider:"),
                ft.Slider(
                    adaptive=True,
                    tooltip=ft.Tooltip(
                        message="Adaptive Slider shows as CupertinoSlider on macOS and iOS and as Slider on other platforms",
                    ),
                ),
            ],
        )
    janela.add( example() )
    print( eslider.value )    
    print( eslider.min )    
    print( eslider.max )    
ft.app(principal)