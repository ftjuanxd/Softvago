import reflex as rx

#Import PC_Navbar
from .navbar_pc import navbar_pc as np
from .navbar_mobile import sidebar as sd

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            np()
        ),
        rx.mobile_and_tablet(
            sd(),
        ),
        background_color="#1E3A8A",
        padding="1em",
        width="100%",
    )