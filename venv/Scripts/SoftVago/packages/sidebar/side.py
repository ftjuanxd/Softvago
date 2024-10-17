import reflex as rx

#Estilos de la web
from ...Style import style

class InputContent(rx.State):

    content : str = ["Location","Work Mode","Salary Range","Available Hours","Position"]

def content(text_value: str):
    return rx.vstack(
        rx.text(text_value,size="4",weight="medium",padding_top="5px"),
        rx.cond(
            text_value == "Word Mode",
                rx.radio(
                    ["On-Site", "Remote", "Hybrid"],
                    direction="column",
                    spacing="2",
                    size="4",
                    weight="medium",
                    variant="surface",
                    color_scheme="blue"
                ),
                rx.cond(
                    rx.slider(
                        default_value=[1000000,2400000],
                        width="100%",
                        min=1000000,
                        max=4000000,
                        color_scheme="blue",
                        bg="gray"
                    ),
                    rx.input(placeholder=f"Enter {text_value}")
                )
        )
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
                        rx.text("Location",size="4",weight="medium"),

                        rx.input(placeholder="Enter Location"),
                        
                        rx.text("Work Mode", size="4", weight="medium"),
                              
                        rx.radio(
                            ["On-Site", "Remote", "Hybrid"],
                            direction="column",
                            spacing="2",
                            size="4",
                            weight="medium",
                            variant="surface",
                            color_scheme="blue"
                        ),

                        rx.text("Salary Range", size="4", weight="medium"),

                         rx.slider(
                            default_value=[1000000,2400000],
                            width="100%",
                            min=1000000,
                            max=4000000,
                            color_scheme="blue",
                            bg="gray"
                        ),

                        rx.text("Avalibe Range", size="4", weight="medium"),

                        rx.input(placeholder="10"),
                        
                        rx.text("Position", size="4", weight="medium"),

                        rx.input(placeholder="10"),

                        rx.button("Apply Filters", on_click=rx.window_alert("Get Started")),

                        align="left",
                        justify="start",
                        padding_x="0.5rem",
                        width="100%",
                        style=style.color_style,
                    ),
                    spacing="5",
                    width="100%",
                ),
        height="100%",
        width="30em",
        margin="-12px",
        padding="1.5em",    
        background_color="#E0E7FF",
    ),