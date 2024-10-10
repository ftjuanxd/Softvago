import reflex as rx
#Import Navbar
from ..packages.navbar import navbar as nv


@rx.page(title="Job Listings")
def index():
    return rx.vstack(
        nv.navbar()
    )
