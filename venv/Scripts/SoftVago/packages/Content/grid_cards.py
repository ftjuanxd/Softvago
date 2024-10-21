import reflex as rx
from .cards import cards as cd

def grid_cards(range:int=12) -> rx.Component:

    return rx.vstack(

        rx.hstack(
            rx.heading(
                "Job Listings",
                size="8",
                weight="bold",
                align="left",
                color="#1E3A8A",
            ),
            width="100%",
            padding="12px"
        ),

        rx.scroll_area(
            rx.grid(
                rx.foreach(
                    rx.Var.range(range),
                    lambda i: cd()
                ),
                gap="1rem",
                grid_template_columns=[
                    "1fr",
                    "repeat(1, 2fr)",
                    "repeat(2, 1fr)",
                    "repeat(3, 1fr)",
                    "repeat(4, 1fr)",
                    "repeat(4, 1fr)",
                ],
                width="100%",
                padding_left="6px",
                padding_right="6px",
                padding_top="2px",
            ), 
            type="always",
            scrollbars="vertical",
            style={"height": "90vh"},
        )
    )