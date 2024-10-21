import reflex as rx

#Estilos de la web
from ..Style import style_component as st

class InputContent(rx.State):

    content : str = ["Location","Work Mode","Salary Range","Available Hours","Position"]

def content(text_value: str):
    return rx.vstack(
        rx.text(text_value, size="4", weight="medium", padding_top="5px"),
        rx.match(
            text_value,
            ("Work Mode",
                rx.radio(
                    ["On-Site", "Remote", "Hybrid"],
                    direction="column",
                    spacing="2",
                    size="4",
                    weight="medium",
                    variant="soft",
                    color_scheme="blue",
                    width="100%",
                )
            ),
            ("Salary Range",
                rx.slider(
                    default_value=[1000000, 2400000],
                    min=1000000,
                    max=4000000,
                    color_scheme="blue",
                    bg="gray",
                    width="100%"
                )
            ),
            rx.input(placeholder=f"Enter {text_value}", width="100%", style=st.style_input_Side),
        ),
        width="100%",
    )

def InputState():
    return rx.foreach(InputContent.content, content)


def sidebar() -> rx.Component:
    return rx.box(
                rx.vstack(
                    rx.vstack(
                        rx.heading(
                            "Filter Jobs", size="7", weight="bold",
                        ),

                        InputState(),

                        rx.button("Apply Filters", on_click=rx.window_alert("Get Started"),style=st.style_button),

                        align="left",
                        justify="start",
                        padding_x="0.5rem",
                        width="100%",
                        style=st.color_style,
                    ),
                    spacing="5",
                    width="100%",
                ),
        height="100vh",
        width="30em",
        padding="1.5em",   
        background_color="#E0E7FF",
    ),