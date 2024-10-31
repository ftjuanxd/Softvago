import reflex as rx

from ..template import template

from ..packages.sidebar import side as sd

from ..packages.Content import grid_cards as gc

@rx.page(title="Job Listings",route="/job")
@template
def index():
    return rx.hstack(
        sd.sidebar(),
        gc.grid_cards(20,height=800),
        width="100%",
    )
