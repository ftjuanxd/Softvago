import reflex as rx

def banner() -> rx.Component:
    return rx.box(
            rx.center(
                rx.section(
                    rx.center(
                        rx.heading(
                            "Find your Dream Job with SoftVago",
                            color="#1E3A8A",
                            size=rx.breakpoints(initial="6", sm="7", md="8", lg="9"),
                            padding="12px",
                        ),
                    ),
                    rx.center(
                        rx.text(
                            "Discover job opportunities that match your skills and preferences.",
                            color="#1F2937",
                            size=rx.breakpoints(sm="2",md="3",lg="5",xl="6")
                            
                        )
                    ),
                    padding_bottom="12px",
                    padding_left="12px",
                    padding_right="12px",
                    background_color="white",
                ),
            ),
        width="100%",
    )