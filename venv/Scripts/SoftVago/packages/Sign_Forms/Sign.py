import reflex as rx
import requests

from ..Style import style_component as st


# Definir el estado para almacenar los inputs y manejar el login
class LoginState(rx.State):
    username: str = ""
    password: str = ""
    
    # Función para actualizar el email
    def set_username(self, value: str):
        self.username = value

    # Función para actualizar la contraseña
    def set_password(self, value: str):
        self.password = value

    # Función para manejar el inicio de sesión
    def handle_login(self):
        login_url = "https://api-softvago.page.resigrass.com.co/Login"
        login_data = {
            "username": self.username,
            "password": self.password
        }
        
        # Hacer la solicitud POST
        response = requests.post(login_url, json=login_data)
        
        if response.status_code == 200:
            # Procesar la respuesta exitosa
            data = response.json()
            print("Inicio de sesión exitoso", data)
            # Redirigir a dashboard
            return rx.redirect("/Dashboard")
        else:
            # Manejar el error
            print(f"Error: {response.status_code}, {response.text}")
            # Puedes mostrar un mensaje de error en la UI
            return rx.alert("Login failed", status="error")


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
                            "Username",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                            color="#1F2937"
                        ),
                        rx.input(
                            rx.input.slot(rx.icon("user"),color=st.color_icon),
                            placeholder="Zone16",
                            type="text",
                            size="3",
                            width="100%",
                            style=st.style_input_filter,
                            on_change=lambda value: LoginState.set_username(value)
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
                            style=st.style_input_filter,
                            on_change=lambda value: LoginState.set_password(value),
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
                        rx.button("Sign In", size="3", width="100%",bg="#60A5FA",on_click=LoginState.handle_login ),
                        rx.button("Sign Up", size="3", width="100%",bg="#1E3A8A",on_click=rx.redirect("/Sign-in")),    
                        ),
                    rx.cond(
                        opc == "Sign Up",
                        rx.center(
                            rx.text("Already registered?", size="3",color="#1F2937"),
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
            ),