import reflex as rx
from .cards import cards as cd

def grid_cards() -> rx.Component:

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
        rx.grid(
            rx.foreach(
                rx.Var.range(12),
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
        ), 
    )