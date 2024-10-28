import reflex as rx
from ..Style.style_component import *

def content()->rx.Component:
    return rx.box(
            rx.vstack(
                rx.card(
                    rx.heading(
                        "Desarrollador Web Full Stack",
                        color="#1E3A8A",
                        size=rx.breakpoints(initial="4", sm="5", md="6", lg="8"),
                        margin_bottom=padding_open_card),
                    rx.hstack(
                        rx.icon("building",color="#60A5FA"),
                        rx.text("InnovaTech Solutions",color="black",size="5",weight="medium",margin_bottom=padding_open_card)
                    ),
                    rx.hstack( #Optimize Components
                        rx.icon("map-pin",color="#60A5FA"),
                        rx.text("Madrid, Espana",color="black"),

                        rx.icon("dollar-sign",color="#60A5FA"),
                        rx.text("$40,000 - $60.000",color="black"),

                        rx.icon("briefcase-business",color="#60A5FA"),
                        rx.text("Remoto",color="black"),
                        spacing="4",
                        margin_bottom=padding_open_card
                    ),
                    rx.text("Buscamos un Desarrollador Web Full Stack apasionado por crear soluciones innovadoras. El candidato ideal tendrá experiencia en tecnologías web modernas y estará dispuesto a trabajar en un entorno dinámico y colaborativo.",margin_bottom=padding_open_card),
                    rx.button("Aplicar ahora", on_click=rx.redirect("/job"),margin_bottom=padding_open_card),                    
                    width="100%",
                    size="4",
                    spacing="3",
                    style=style_card_open,
                ),
                rx.card(
                    rx.heading(
                        "Descripcion del Trabajo",
                        color="#1E3A8A",
                        size=rx.breakpoints(initial="3", sm="4", md="5", lg="6"),
                        margin_bottom=padding_open_card),
                    rx.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eu sem cursus, convallis dolor in, molestie elit. Etiam consequat porttitor massa. Ut malesuada ornare magna, sed malesuada lectus convallis vel. Mauris pulvinar, quam at tincidunt facilisis, mi diam porttitor ligula, feugiat efficitur leo libero sed mi. Nulla tristique a nisl ac feugiat. Etiam laoreet, enim a finibus vulputate, dolor enim semper nulla, sit amet cursus elit mauris at magna. Aliquam erat volutpat. Praesent ut lacinia lacus. Suspendisse potenti. Duis in consequat velit. In tempor est non dui vulputate volutpat.",margin=padding_open_card),
                    margin_top=padding_open_card,
                    size="4",
                    width="100%",
                    bg="#CED7F2",
                    color="#1F2937"
                ),
                  rx.card(
                    rx.heading(
                        "Requisitos",
                        color="#1E3A8A",
                        size=rx.breakpoints(initial="3", sm="4", md="5", lg="6"),
                        margin_bottom=padding_open_card),
                    rx.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam eu sem cursus, convallis dolor in, molestie elit. Etiam consequat porttitor massa. Ut malesuada ornare magna, sed malesuada lectus convallis vel. Mauris pulvinar, quam at tincidunt facilisis, mi diam porttitor ligula, feugiat efficitur leo libero sed mi. Nulla tristique a nisl ac feugiat. Etiam laoreet, enim a finibus vulputate, dolor enim semper nulla, sit amet cursus elit mauris at magna. Aliquam erat volutpat. Praesent ut lacinia lacus. Suspendisse potenti. Duis in consequat velit. In tempor est non dui vulputate volutpat.",margin=padding_open_card),
                    size="4",
                    style=style_card_open,
                    width="100%",
                ),
            ),
        width="70%",
        padding="1.5em",
    )
