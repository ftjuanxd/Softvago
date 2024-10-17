from typing import Callable

import reflex as rx

from .packages.navbar import navbar as nv

from .packages.footer import footer as ft

def template(page:Callable[[],rx.Component]) -> rx.Component:
    return rx.vstack(
        nv.navbar(),
        rx.vstack(
            page(),
        ),
        ft.footer(),
        width="100%"
    )