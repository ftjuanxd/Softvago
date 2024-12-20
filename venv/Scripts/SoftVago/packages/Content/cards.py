import reflex as rx
import os

#Si la direccion de la imagen es dinamica y cambiante se usa esto rx.get_upload_url(#link o url) 

def cards(propuesta="Analista de Datos",empresa="Google",location="Remote",Hours="Full-time",Salary="$100k - $130k",opc="") -> rx.Component:

    return rx.card(
            rx.vstack(
                rx.flex(
                    rx.heading(propuesta, size="6",color="#1E3A8A"),
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
                        rx.button("Ver mas",on_click=rx.redirect("/Card_Open")),
                        direction="column",
                    ),
                    direction="row",    
                    justify="between",
                    width="100%",
                ),
                width="47vh",#47
            ),
            margin_bottom="12px"
        )
