import reflex as rx
from styles.colors import Color as Color
from styles.colors import TextColor as TextColor
from styles.styles import Size,Spacing

def info_text(title:str,body: str) -> rx.Component:
    return rx.box(
        rx.text(
            title,
            color=Color.PRIMARY.value, 
            weight="bold",
            as_="span"
        ),
        rx.text(body),
        color=TextColor.BODY.value
    )