from django.apps import AppConfig


class CustomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Custome'

    def ready(self):
        import Custome.signals
        