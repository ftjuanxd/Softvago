import reflex as rx

from ..template import template

from ..packages.Sign_Forms import Sign as sg

@rx.page(title="Sign In",route="/Sign-in")
@template
def index():
    return rx.center(
        sg.sign("Sign In"),
        width="100vw"
    )
      