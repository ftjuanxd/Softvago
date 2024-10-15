import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium",color="White"), href=url
    )

def navbar_pc() -> rx.Component:
    return   rx.hstack(
                rx.hstack(
                    rx.flex(
                        rx.icon("computer",stroke_width=3),
                        gap = "2",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "SoftVago", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("Job Listings", "/job"),
                    navbar_link("Sign In", "/"),
                    navbar_link("Sign Up", "/job"),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            )