from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name = "Профили"
    def ready(self):
        from . import signals

