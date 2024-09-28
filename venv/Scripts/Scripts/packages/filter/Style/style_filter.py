import reflex as rx

#hacer comentario con ctrl + k + c
#quitar comentario con ctrl + k + u


padding_inputs = "12px",
color = " #94A3B8",
style_input_filter = dict(
    backgroundColor="white",
    border="1px solid #94A3B8",
    color="black",
)

style_input = style_input_filter| dict(
    margin_right = padding_inputs,

)
style_select = dict(
    color="white",
    background_color="white",
    border_color="#94A3B8",
    variant="soft",
    radius="large",
)
style_placeholder = {
    "_placeholder": {
        "color": "black",
        "font_weight": "500",
    },
}