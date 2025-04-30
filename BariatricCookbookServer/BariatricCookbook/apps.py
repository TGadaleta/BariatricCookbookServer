from django.apps import AppConfig


class BariatriccookbookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BariatricCookbook'

    def ready(self):
        import BariatricCookbook.signals
