from django.apps import AppConfig

MODULE = __name__
APP = MODULE[: MODULE.rfind(".")]


class AutoFunctionsConfig(AppConfig):
    name = APP

    def ready(self):
        from . import serializers
