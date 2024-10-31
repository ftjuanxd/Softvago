import reflex as rx
from ..components.stats_cards import stats_cards_group
from ..packages.dashboard.navbar import navbar
from ..packages.dashboard.table import main_table
from ..packages.Sign_Forms.State import LoginState

@rx.page(title="DashBoard", route="/Dashboard")
def index() -> rx.Component:

     # Verificar si el usuario está autenticado
    if not LoginState.is_authenticated():
        # Redirigir al login si no está autenticado
        return rx.redirect("/Sign-in")

    return rx.vstack(
        navbar(),
        stats_cards_group(),
        rx.box(
            main_table(),
            width="100%",
        ),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
    )