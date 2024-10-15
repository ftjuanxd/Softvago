import reflex as rx

def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem", 
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4), 
                    "color": rx.color("accent", 11),
                },
                "color":"white",
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Home", "library-big", "/"),
        sidebar_item("Job Listings", "text-search", "/job"),
        sidebar_item("Sign In", "log-in", "/"),
        sidebar_item("Sign Up", "user-plus", "/job"),
        spacing="1", 
        width="100%",
    )


def sidebar() -> rx.Component:
    return rx.box(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        rx.vstack(
                            rx.box(
                                rx.drawer.close(
                                    rx.icon("x", size=30)
                                ),
                                width="100%",
                            ),
                            rx.hstack(
                                rx.icon(
                                    "computer",#/favicon.ico",
                                    width="2.25em",
                                    height="auto",
                                    border_radius="25%",
                                ),
                                rx.heading(
                                    "SoftVago", size="7", weight="bold"
                                ),
                                align="center",
                                justify="start",
                                padding_x="0.5rem",
                                width="100%",
                            ),
                            sidebar_items(),
                            spacing="5",
                            width="100%",
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        background_color="#1E3A8A",
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),