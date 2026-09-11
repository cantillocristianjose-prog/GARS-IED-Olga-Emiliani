import reflex as rx
import styles.styles as styles
import views.utils as utils
from routers import Route
from styles.styles import Size
from styles.colors import Color
from components.navbar import navbar
from views.header import header
from views.creditos_info import creditos_info


@rx.page(
    route=Route.CREDITOS.value,
    title=utils.creditos_title,
    description=utils.creditos_descripcion,
    image=utils.preview,
    meta=utils.creditos_meta
)

def creditos() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                #header(),
                creditos_info(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        )
    )