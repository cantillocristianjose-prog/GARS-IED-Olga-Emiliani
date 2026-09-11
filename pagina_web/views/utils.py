import reflex as rx
#Comun

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "https://www.infobae.com/america/perrosygatos/2022/01/03/8-datos-curiosos-que-desconocemos-de-los-gatos/"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview}
]



#Index

index_title = "Gestion Analisis y Resgistro de Saber 11"
index_descripcion = ""

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_descripcion}
]

index_meta.extend(_meta)
#Creditos

creditos_title = "GARS | creditos"
creditos_descripcion = ""

creditos_meta = [
    {"name": "og:title", "content": creditos_title},
    {"name": "og:description", "content": creditos_descripcion}
]
creditos_meta.extend(_meta)

