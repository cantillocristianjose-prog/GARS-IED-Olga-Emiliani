import reflex as rx

config = rx.Config(
    app_name="pagina_web",
    cors_allowed_origins=[
        "https://localhost:3000",
        "https://gars-web.vercel.app"
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ],
    api_url="http://apithe.up.railway.app"
)