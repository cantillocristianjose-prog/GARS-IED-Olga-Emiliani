import reflex as rx
from styles.colors import Color
from styles.fonts import Font
from styles.colors import TextColor
from enum import Enum
#Constantes
MAX_WIDTH = "600px"
FADEIN_ANIMATION = "animate__animated animate__fadeIn"
TADA_ANIMATION = "animate__animated animate__tada"

#Spacings
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    MEDIUM_SMALL = "2"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
    VERY_BIG = "9"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Rasmus+Andersson:wght@400&display=swap",
    "https://fonts.googleapis.com/css2?family=Open+Sans:wght@400&display=swap",
    "https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css" #link de esta aplicacion https://animate.style
    #"/css/styles.css"
]



BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background_color":Color.BACKGROUND.value,
    rx.heading: {
        "size":"7",
        "color":TextColor.HEADER.value,
        "font_family": Font.TITLE.value
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color":TextColor.HEADER.value,
        "background_color":Color.PRIMARY.value,
        "white_space": "normal",
        "text_align":"start",
        "_hover": {
            "background_color":Color.SECONDARY.value
        }
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

nabvar_title_style = dict(
    font_family=Font.LOGO.value,
    font_size=Size.LARGE.value
)

title_style = dict(
    width="100%",
    size="7",
    padding_top=Size.DEFAULT.value
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_body_style = dict(
    font_family=Font.DEFAULT.value,
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)