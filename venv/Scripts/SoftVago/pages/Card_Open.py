import reflex as rx

from ..template import template

from ..packages.Card_Open import Content as ct

from ..packages.Content import grid_cards as gd

@rx.page(title="Job Listings",route="/Card_Open")
@template
def index():
    return rx.hstack(
        ct.content(),
        gd.grid_cards(4,"open"),
        width="100vw",
        margin_top="-12px",
        margin_bottom="-19px"
    )
