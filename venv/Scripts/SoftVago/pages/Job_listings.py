import reflex as rx

from ..template import template

from ..packages.sidebar import side as sd

@rx.page(title="Job Listings",route="/job")
@template
def index():
    return rx.vstack(
        rx.flex(
            sd.sidebar(),
            width="100%"
        )
    )
