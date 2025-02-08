import flet as ft

def principal( janela:ft.Page ):
    janela.add( ft.Tabs(
        selected_index=0,
        animation_duration=300,
        width=int(0.8 * janela.window.width),
        height=int(0.8 * janela.window.height),
        divider_color=ft.colors.GREEN,
        tabs=[
            ft.Tab(
                text="Tab 1",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3", text_align=ft.TextAlign.CENTER),
            ),
            ft.Tab(
                text="Tab 4",
                icon=ft.icons.ADD_BOX,
                content=ft.Container( 
                    bgcolor=ft.colors.RED,
                    content= ft.Row(
                        controls=[                
                            ft.Text(
                                "TAB 4",
                                text_align=ft.TextAlign.CENTER,
                                color=ft.colors.BROWN,
                                size=32,
                                bgcolor="yellow",
                                expand=True,
                                font_family="Helvetic",
                                italic=True,
                                scale=ft.Scale(10, 10),
                                rotate=ft.Rotate(0.05)  # radianos
                            ),
                        ],
                        expand=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ),
            )
        ],
    ),)
ft.app( principal )