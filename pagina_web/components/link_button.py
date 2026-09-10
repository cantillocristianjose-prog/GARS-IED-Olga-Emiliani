import reflex as rx
import styles.styles as styles
from styles.styles import Size,Spacing

def link_button(title:str,body: str, image: str ,url:str,is_external = True,animated=False,avarca="100%") -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.VERY_BIG.value,
                    height=Size.VERY_BIG.value,
                    margin=Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title,style=styles.button_title_style),
                    rx.text(body,style=styles.button_body_style),
                    spacing=Spacing.VERY_SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value,
                    margin=Size.SMALL.value,
                    align="start",
                ),
                width="100%"
            )
        ),
        href=url,
        is_external=is_external,
        class_name=styles.TADA_ANIMATION if animated else None,
        width=avarca
    )