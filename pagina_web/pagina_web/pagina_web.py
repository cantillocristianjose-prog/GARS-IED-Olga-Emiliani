"""Ctrl + Shift + P y poner "Python: Select Interpreter" y seleccionar el interprete de python que diga venv"""
import reflex as rx
import styles.styles as styles
from pages.index import index
from pages.creditos import creditos


app = rx.App(
    style=styles.BASE_STYLE,
    stylesheets=styles.STYLESHEETS
)