from typing import Callable

import reflex as rx

from .packages.navbar import navbar as nv

from .packages.footer import footer as ft

def template(page:Callable[[],rx.Component]) -> rx.Component:
    return rx.vstack(
        nv.navbar(),
        rx.vstack(
            page(),
            margin_top="-12px",
            margin_bottom="-24px"
        ),
        ft.footer(),
        width="100%"
    )