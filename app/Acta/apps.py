from django.apps import AppConfig


class ActaConfig(AppConfig):
    # pyrefly: ignore  # bad-override
    default_auto_field = "django.db.models.BigAutoField"
    name = "app.Acta"
