import reflex as rx


from ..template import template
#Importat Banner/Section
from ..packages.section import section as dn
#Import Buscador
from ..packages.filter import filter as sh
#Import Cards
from ..packages.Content import grid_cards as gc

@rx.page(title="SoftVago",route="/")
@template
def index():
    return rx.vstack(
        dn.banner(),
        sh.filter(),
        gc.grid_cards(),
        width ="100%"
    )