import reflex as rx
from .cards import cards as cd

def grid_cards(range:int=12, opc:str="no_open",height:int=600) -> rx.Component:

    return rx.vstack(
        rx.cond(
            opc == "no_open",
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
        ),       

        rx.cond(
            opc=="no_open",
            rx.scroll_area(
                rx.grid(
                    rx.foreach(
                        rx.Var.range(range),
                        lambda i: cd(opc=opc)
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
                type="hover",
                scrollbars="vertical",
                style={"height":height},
                width="100%"
            ),
            rx.grid(
                rx.foreach(
                    rx.Var.range(range),
                    lambda i: cd(),
                ),
                columns="1",
                margin_top="25px",
                width="100%"
            ),
        )
        
    )