import reflex as rx

from ..template import template

from ..packages.Sign_Forms import Sign as sg

@rx.page(title="Sign Up",route="/Sign-Up")
@template
def index():
    return rx.center(
        sg.sign("Sign Up"),
        width="100vw"
    )
       