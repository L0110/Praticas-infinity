import flet as ft


def main(page: ft.Page):
    
    def handle_menu_item_click(e):
        print(f"{e.control.content.value}.on_click")
        page.open(ft.SnackBar(content=ft.Text(f"{e.control.content.value} foi clicado!")))
        page.update()

    def handle_submenu_open(e):
        print(f"{e.control.content.value}.on_open")

    def handle_submenu_close(e):
        print(f"{e.control.content.value}.on_close")

    def handle_submenu_hover(e):
        print(f"{e.control.content.value}.on_hover")

    menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.center,
            bgcolor={
                ft.ControlState.HOVERED: ft.colors.LIGHT_BLUE_200,
                ft.ControlState.FOCUSED: ft.colors.LIGHT_BLUE_400,
                ft.ControlState.DEFAULT: ft.colors.WHITE,
            },
            shadow_color=ft.colors.LIGHT_BLUE_100,
            surface_tint_color=ft.colors.ORANGE_100,
            padding=0,
            elevation=0,
            #shape=ft.StadiumBorder(),
            #shape=ft.BeveledRectangleBorder(radius=5),
            shape=ft.RoundedRectangleBorder(radius=5),
            side=ft.BorderSide(
                color=ft.colors.RED_600,
                width=2,              
            ),
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("File"),
                style=ft.ButtonStyle(
                    color=ft.colors.YELLOW
                ),
                on_open=handle_submenu_open,
                on_close=handle_submenu_close,
                on_hover=handle_submenu_hover,
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("About"),
                        leading=ft.Icon(ft.icons.INFO),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}
                        ),
                        on_click=handle_menu_item_click,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Save"),
                        leading=ft.Icon(ft.icons.SAVE),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}
                        ),
                        on_click=handle_menu_item_click,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Quit"),
                        leading=ft.Icon(ft.icons.CLOSE),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}
                        ),
                        on_click=handle_menu_item_click,
                    ),
                ],
            ),
            ft.SubmenuButton(
                content=ft.Text("View"),
                on_open=handle_submenu_open,
                on_close=handle_submenu_close,
                on_hover=handle_submenu_hover,
                controls=[
                    ft.SubmenuButton(
                        content=ft.Text("Zoom"),
                        controls=[
                            ft.MenuItemButton(
                                content=ft.Text("Magnify"),
                                leading=ft.Icon(ft.icons.ZOOM_IN),
                                close_on_click=False,
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.ControlState.HOVERED: ft.colors.PURPLE_200
                                    }
                                ),
                                on_click=handle_menu_item_click,
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Minify"),
                                leading=ft.Icon(ft.icons.ZOOM_OUT),
                                close_on_click=False,
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.ControlState.HOVERED: ft.colors.PURPLE_200
                                    }
                                ),
                                on_click=handle_menu_item_click,
                            ),
                        ],
                    )
                ],
            ),
        ],
    )

    page.add(ft.Row([menubar]))


ft.app(main)