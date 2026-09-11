import reflex as rx
import datetime
from styles.fonts import Font
#from components.title import title
from styles.colors import TextColor
from styles.colors import Color
from components.link_button import link_button
from styles.styles import Size,Spacing

def header() -> rx.Component:
    return rx.vstack(
        rx.center(
            # rx.box(
            #     rx.text("hola mundo"),
            #     background_color=Color.CONTENT.value,
            # )
        ),
        spacing=Spacing.BIG.value,
        align="start",
    )