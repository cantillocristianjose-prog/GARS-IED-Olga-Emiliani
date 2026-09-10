import reflex as rx
import styles.styles as styles
import views.utils as utils
from styles.styles import Size
from styles.colors import Color
from components.navbar import navbar
from views.header import header
from views.index_info import index_info



# los iconos son sacado de https://fontawesome.com/
@rx.page(
    title=utils.index_title,
    description=utils.index_descripcion,
    image=utils.preview,
    meta=utils.index_meta
)

def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(

                ),
                # index_info(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        )
    )