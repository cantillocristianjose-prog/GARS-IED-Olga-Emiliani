import reflex as rx
import styles.styles as styles
from styles.colors import Color as Color
from styles.colors import TextColor as TextColor
from styles.styles import Size,Spacing
from routers import Route
import styles.styles as styles
def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
        rx.text(
            "GARS",
            style=styles.nabvar_title_style,
            color=TextColor.HEADER.value,as_="span"
        ),
        href=Route.INDEX.value
        ),
        position="sticky",
        bg=Color.PRIMARY.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        width="100%",
        top="0",
    )