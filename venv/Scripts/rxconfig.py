import reflex as rx


class AppConfig(rx.Config):
    pass

config = AppConfig(
    app_name="SoftVago",
    db_url="http://SoftVago.com:8000",
    env=rx.Env.DEV,
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    },
)
