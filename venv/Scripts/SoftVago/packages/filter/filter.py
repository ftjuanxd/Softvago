import reflex as rx

from ..Style import style_component as sf

# Crear la interfaz de usuario
def filter():
    return rx.container(
        rx.vstack(
            rx.box(
                rx.input(
                    placeholder="Search for jobs...",
                    width="100%",
                    style = {**sf.style_input_filter,**sf.style_placeholder}
                ),
                rx.button("Get Started", on_click=rx.window_alert("Get Started"),position="absolute",top="11px",right="12px",z_index="1"),
                position="relative",
                width="100%",
                padding="12px",
            ),
            width="100%",
        ),
        #Filtros Adiccionales
        rx.hstack(
            rx.center(
                rx.input(placeholder="Location",style = {**sf.style_input,**sf.style_placeholder},
                margin_left="14px"),
                rx.box(
                    rx.select(
                        ["Remote", "On-site", "Hybrid"], 
                        placeholder="Work Mode",
                        label="Work Mode",
                        **sf.style_select
                    ),
                    margin_right="12px",
                ),
                rx.input(placeholder="Salary Range",style = {**sf.style_input,**sf.style_placeholder}),
                rx.input(placeholder="Position/Title",style = {**sf.style_input,**sf.style_placeholder}),
                rx.input(placeholder="Hours",style = {**sf.style_input,**sf.style_placeholder}),
            ),
            padding_left="12px",
        ),
        align="center",
        spacing="20px",
        padding="12px",
        width="100%",
    )