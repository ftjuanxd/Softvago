import reflex as rx

from ..template import template

from ..packages.Sign_Forms import Sign as sg

@rx.page(title="Sign In",route="/Sign-in")
@template
def index():
    return rx.stack(
        sg.sign("Sign In"),
        margin_y="158px",
        padding_bottom="2.3em",
        align="center",
        justify="center",
        width="100vw"
    )
      