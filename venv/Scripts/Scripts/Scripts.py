import reflex as rx

#Estilos de la web
from .Style import style
#Import main
from .Screen import main as mn

@rx.page(title="SoftVago")
def index():
    return mn.index()

app = rx.App(style=style.style_background)
app.add_page(index)
