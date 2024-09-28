import reflex as rx
#Importar navbar
from .packages.navbar import navbar as nv
#Importat Banner/Section
from .packages.section import section as dn
#Import Buscador
from .packages.filter import filter as sh
#Import Cards
from .packages.Content import grid_cards as gc
#Import Footer
from .packages.footer import footer as ft
#Estilos de la web
from .Style import style

@rx.page(title="SoftVago")
def index():
    return rx.vstack(
        nv.navbar(),
        dn.banner(),
        sh.filter(),
        gc.grid_cards(),
        ft.footer(),
    )

app = rx.App(style=style.style_background)
app.add_page(index)
