import reflex as rx

from ..template import template

from ..packages.Sign_Forms import Sign as sg

@rx.page(title="Sign Up",route="/Sign-Up")
@template
def index():
    return rx.stack(
            sg.sign("Sign Up"),
            margin_y="106px",
            align="center",
            justify="center",
            width="100vw"
        )
    
       