import reflex as rx

#hacer comentario con ctrl + k + c
#quitar comentario con ctrl + k + u

color_style = { "color":"#1E3A8A"}
padding_inputs = "12px",
color = "#94A3B8",
color_icon="#0a8bbf",
shadow="rgba(0, 0, 0, 0.15) 0px 6px 16px"

style_button = dict(
    background = "#60A5FA",
    height="36px",
    border_radius="6px",
)

#Style filters
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
        "color": "#000",
        "font_weight": "500",
    },
}

#Style Side

style_input_Side = style_placeholder |  {
    "input":{
        "background":"#fff",
        "color":"#000"
    }
}

#Style Card-Open
padding_open_card = ".5em"
style_card_open = {
    "box_shadow":shadow,
    "color":"#1F2937"
}