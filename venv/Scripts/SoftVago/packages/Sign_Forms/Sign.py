import reflex as rx
import requests

from ..Style import style_component as st
from .State import LoginState
from .State import RegisterState

def sign(opc: str) -> rx.Component:
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
                    rx.hstack(
                        rx.vstack(
                            # Name
                            rx.text(
                                "Name",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                                color="#1F2937"
                            ),
                            rx.input(
                                rx.input.slot(rx.icon("type"), color=st.color_icon),
                                placeholder="Daniel Hernando",
                                type="text",
                                size="3",
                                width="100%",
                                style=st.style_input_filter,
                                on_change=lambda value: RegisterState.set_name(value),
                            ),
                        ),
                        rx.vstack(
                            # Last Name
                            rx.text(
                                "Last Name",
                                size="3",
                                weight="medium",
                                text_align="left",
                                width="100%",
                                color="#1F2937"
                            ),
                            rx.input(
                                rx.input.slot(rx.icon("type"), color=st.color_icon),
                                placeholder="Perez",
                                type="text",
                                size="3",
                                width="100%",
                                style=st.style_input_filter,
                                on_change=lambda value: RegisterState.set_lastName(value),
                            ),
                        ),
                    ),
                    # Email
                    rx.text(
                        "Email",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                        color="#1F2937"
                    ),
                    rx.input(
                        rx.input.slot(rx.icon("mail"), color=st.color_icon),
                        placeholder="placeholder@gmail.com",
                        type="email",
                        size="3",
                        width="100%",
                        style=st.style_input_filter,
                        on_change=lambda value: RegisterState.set_email(value),
                    ),
                    justify="start",
                    spacing="4",
                    width="100%",
                ),
            ),
            rx.vstack(
                rx.text(
                    "Username",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                    color="#1F2937"
                ),
                rx.input(
                    rx.input.slot(rx.icon("user"), color=st.color_icon),
                    placeholder="Zone16",
                    type="text",
                    size="3",
                    width="100%",
                    style=st.style_input_filter,
                    on_change=lambda value: LoginState.set_username(value) if opc == "Sign In" else RegisterState.set_username(value),
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
                    rx.input.slot(rx.icon("lock"), color=st.color_icon),
                    placeholder="Enter your password",
                    type="password",
                    size="3",
                    width="100%",
                    style=st.style_input_filter,
                    on_change=lambda value: LoginState.set_password(value) if opc == "Sign In" else RegisterState.set_password(value),
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
                rx.button("Sign In", size="3", width="100%", bg="#60A5FA", on_click=LoginState.handle_login),
                rx.button("Sign Up", size="3", width="100%", bg="#1E3A8A", on_click=RegisterState.handle_register),
            ),
            rx.cond(
                opc == "Sign Up",
                rx.center(
                    rx.text("Already registered?", size="3", color="#1F2937"),
                    rx.link("Sign in", href="/Sign-in", size="3"),
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
    )
