import reflex as rx

from ..Sign_Forms.State import LoginState

def navbar():
    return rx.flex(
        rx.badge(
            rx.icon(tag="square-chevron-right", size=28),
            rx.heading("SoftVago", size="6"),
            color_scheme="blue",
            radius="large",
            align="center",
            variant="surface",
            padding="0.65rem",
        ),
        rx.spacer(),
        rx.hstack(
            rx.color_mode.button(),
            rx.icon(tag="power",on_click=LoginState.logout,color="crimson",cursor=""),
            align="center",
            spacing="3",
            
        ),
        spacing="2",
        flex_direction=["column", "column", "row"],
        align="center",
        width="100%",
        top="0px",
        padding_top="2em",
    )
