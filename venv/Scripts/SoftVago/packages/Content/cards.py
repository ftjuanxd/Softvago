import reflex as rx
import os

#Si la direccion de la imagen es dinamica y cambiante se usa esto rx.get_upload_url(#link o url) 

def cards(propuesta="Analista de Datos",img="/fondo.jpg",empresa="Google",location="Remote",Hours="Full-time",Salary="$100k - $130k") -> rx.Component:

    return rx.card(
            rx.vstack(
                rx.image(
                    src=img,
                    width="70%",
                    height="auto",
                    border_radius="10px",
                    padding_right="25px"
                ),
                rx.flex(
                    rx.heading(propuesta, size="4", mb="1",color="#1E3A8A"),
                    direction="row",
                    justify="between",
                    width="100%",
                ),
                rx.text(
                    empresa," - ",location,
                    size="2",
                    mb="6",
                    color="#1F2937",
                ),
                rx.text(
                    Hours," - ",Salary,
                    size="2",
                    mb="1",
                    color="#1F2937",
                ),
                rx.divider(width="100%"),
                rx.flex(
                    rx.flex(
                        rx.button("Ver mas"),
                        direction="column",
                    ),
                    direction="row",
                    justify="between",
                    width="100%",
                ),
                width="47vh",#47
            ),
        )
