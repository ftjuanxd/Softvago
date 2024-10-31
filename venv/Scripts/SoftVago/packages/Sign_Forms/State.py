import reflex as rx
import requests
from datetime import datetime

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
        
    def is_authenticated(self) -> bool:
        """Verifica si el usuario está autenticado."""
        return bool(self.token)

    def logout(self):
        """Cierra la sesión y redirige al usuario al login."""
        self.token = ""  # Limpiar el token para cerrar sesión
        return rx.redirect("/Sign-in")  # Redirigir a la página de inicio de sesión


class RegisterState(rx.State):
    name: str = ""
    lastname: str = ""
    email: str = ""
    username: str = ""
    password: str = ""
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJiYXNlV2ViQXBpU3ViamVjdCIsImp0aSI6IjM2YjJiMjQxLWNiYjYtNGZkNS04NWJmLTQxMWNkM2U5NTA2YSIsImlhdCI6IjE3MzA0MTc4OTUiLCJVc2VybmFtZSI6WyJqb2hhbiIsImpvaGFuIl0sImV4cCI6MTczMDUwNDI5NSwiaXNzIjoic29mdHZhZ28uY29tLmNvIiwiYXVkIjoiYXRvbXBvcGV6LmNvbS5jbyJ9.IO1bSaR1K-938W_YdPmtmxa3ZQHOxnJsnl8YSpk2Kxw"
    register_url = "https://api-softvago.page.resigrass.com.co/PostUsers"
    
    def set_name(self, value: str):
        self.name = value

    def set_lastName(self, value: str):
        self.lastname = value

    def set_email(self, value: str):
        self.email = value

    def set_username(self, value: str):
        self.username = value

    def set_password(self, value: str):
        self.password = value


    def handle_register(self) -> rx.Component:
        data = {
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "registrationDate":datetime.now().strftime("%Y-%m-%d"),
            "idRol": 2,
            "enable": True,
            "login": {
                "username": self.username,
                "password": self.password
            }
        }
        headers = {}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        response = requests.post(self.register_url, json=data, headers=headers)

        # Imprimir información de la respuesta para depuración
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")

        if response.status_code == 200:
            # Aquí verificamos si el contenido es un mensaje de éxito
            if response.text == "Usuario creado exitosamente":
                print("Usuario creado exitosamente")
                return rx.redirect("/Sign-in")
            else:
                print("Error: La respuesta no es un JSON válido.")
                return rx.alert("Error: La respuesta del servidor no es válida.", status="error")
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return rx.alert(f"Operation failed: {response.text}", status="error")