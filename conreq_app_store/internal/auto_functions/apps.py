from django.apps import AppConfig

MODULE = __name__
APP = MODULE[: MODULE.rfind(".")]


class AutoFunctionsConfig(AppConfig):
    name = APP

    def ready(self):
        # pylint: disable=import-outside-toplevel, unused-import
        from .deserializers import deserialize_all

        deserialize_all()

        from . import serializers
