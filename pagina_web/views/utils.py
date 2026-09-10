import reflex as rx
from datetime import datetime,timezone,timedelta
#Comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "https://www.infobae.com/america/perrosygatos/2022/01/03/8-datos-curiosos-que-desconocemos-de-los-gatos/"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview}
]



#Index

index_title = "El cuartel de TheObsidianBoy"
index_descripcion = "Hola mi nombre es TheObsidianBoy y soy creador de contenido"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_descripcion}
]

index_meta.extend(_meta)
#Videos

libros_title = "TheObsidianBoy | Libros"
libros_descripcion = "este es un listado de mis libros"

videos_meta = [
    {"name": "og:title", "content": libros_title},
    {"name": "og:description", "content": libros_descripcion}
]
videos_meta.extend(_meta)

