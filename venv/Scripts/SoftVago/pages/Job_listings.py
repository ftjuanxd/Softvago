import reflex as rx

from ..template import template

@rx.page(title="Job Listings",route="/job")
@template
def index():
    return rx.vstack(
        rx.heading("Job Listings")
    )
