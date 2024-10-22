import reflex as rx

from ..Style import style_component as st

def sign(opc:str) -> rx.Component:
    return rx.card(
                rx.vstack(
                    rx.center(
                        rx.heading(
                            opc,
                            size="8",
                            as_="h2",
                            text_align="center",
                            width="100%",
                            style=st.color_style
                        ),
                        direction="column",
                        spacing="5",
                        width="100%",
                    ),
                    rx.cond(
                        opc == "Sign Up",
                        rx.vstack(
                            rx.text(
                                "Full Name",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                                color="#1F2937"
                            ),
                            rx.input(
                                rx.input.slot(rx.icon("type"),color=st.color_icon),
                                placeholder="Daniel Hernando Perez",
                                type="text",
                                size="3",
                                width="100%",
                                style=st.style_input_filter
                            ),
                            justify="start",
                            spacing="2",
                            width="100%",
                        ),
                    ),
                    rx.vstack(
                        rx.text(
                            "Email address",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                            color="#1F2937"
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("user"),color=st.color_icon),
                            placeholder="user@reflex.dev",
                            type="email",
                            size="3",
                            width="100%",
                            style=st.style_input_filter
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.text(
                            "Password",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                            color="#1F2937"
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("lock"),color=st.color_icon),
                            placeholder="Enter your password",
                            type="password",
                            size="3",
                            width="100%",
                            style=st.style_input_filter
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),
                    rx.cond(
                        opc == "Sign In",
                        rx.hstack(
                            rx.checkbox(
                                "Remember Me",
                                spacing="2",
                                color_scheme="blue",
                                color="#1F2937"
                            ),
                            rx.container(
                                rx.link("Forgot Password?", href="#", size="3"),
                                text_align="right",
                                padding="-8px"
                            ),
                            width="100%",
                        ),
                    ),
                    rx.cond(
                        opc == "Sign In",
                        rx.button("Sign In", size="3", width="100%",bg="#60A5FA"),
                        rx.button("Sign Up", size="3", width="100%",bg="#1E3A8A"),    
                        ),
                    rx.cond(
                        opc == "Sign In",
                        rx.center(
                            rx.text("Already registered?", size="3",color="#1F2937"),
                            rx.link("Sign in", href="#", size="3"),
                            opacity="0.8",
                            spacing="2",
                            direction="row",
                            width="100%",
                        ),
                    ),
                    spacing="6",
                    width="100%",
                ),
                max_width="28em",
                size="4",
                width="100%",
            ),