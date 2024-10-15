import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
            rx.flex(
                rx.hstack(
                    rx.icon(
                        "computer",
                        stroke_width=3,
                        src="../../../assets/favicon.ico",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.vstack(
                        rx.text(
                            "SoftVago",
                            size="6",
                            white_space="nowrap",
                            weight="medium",
                        ),
                        rx.text(
                            "Connecting talent with opportunities.",
                            size="4",
                            white_space="nowrap",
                            weight="medium",
                        ),
                    ),
                    spacing="2",
                    align="center",
                    width="100%",
                    padding="16px",
                    background_color="#1E3A8A",
                ),
            ),
            spacing="5",
            width="100%",
        )