from django.apps import AppConfig


class VacinacaoConfig(AppConfig):
    name = 'vacinacao'

    def ready(self):
        from . import signals  # noqa: F401
