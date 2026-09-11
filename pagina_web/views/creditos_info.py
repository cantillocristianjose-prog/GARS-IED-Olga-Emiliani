import reflex as rx
from routers import Route
from styles.styles import Size,Spacing
from components.link_button import link_button
from components.title import title
from components.info_text import info_text
from styles.colors import Color

def creditos_info() -> rx.Component:
    return rx.vstack(
        title("Nexus Analitica"),

        rx.box(
            info_text(
                "Equipo conforado por: ",
                """
                Hellen Rivera (CEO),

                Adriana Morales (Analista de datos),

                Breiner Coronell (Marketing),

                Jeanndel Rodrigez (Progamador),

                Cristian Cantillo (Progamador)
                """
            ),
            border_radius="10px",
            background_color=Color.BACKGROUND_BOX.value,
            padding=Size.DEFAULT.value,
            width="100%"
        ),

        width="100%"
    )