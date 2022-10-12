from django.apps import AppConfig


class CommerceappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'commerceapp'

    def ready(self):
        import commerceapp.signals