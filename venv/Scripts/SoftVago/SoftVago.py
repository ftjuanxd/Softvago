import reflex as rx

#Estilos de la web
from .Style import style

app = rx.App(style=style.style_background,stylesheets=["https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"])
