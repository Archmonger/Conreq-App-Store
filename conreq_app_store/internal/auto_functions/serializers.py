from django.conf import settings
from django.core.serializers import serialize
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..app_store import models

MODELS_DIR = getattr(settings, "MODELS_DIR")

# pylint: disable=unused-argument,missing-function-docstring


def serialize_model(model):
    data = serialize("json", model.objects.all())
    with open(MODELS_DIR / f"{model.__name__}.json", "w", encoding="utf-8") as fp:
        fp.write(data)


@receiver(post_save, sender=models.Category)
def category(sender, **kwargs):
    serialize_model(sender)


@receiver(post_save, sender=models.Subcategory)
def subcategory(sender, **kwargs):
    serialize_model(sender)


@receiver(post_save, sender=models.ConreqPackage)
def conreq_package(sender, **kwargs):
    serialize_model(sender)


@receiver(post_save, sender=models.EnvironmentVariable)
def enviroment_variables(sender, **kwargs):
    serialize_model(sender)


@receiver(post_save, sender=models.Screenshot)
def screenshot(sender, **kwargs):
    serialize_model(sender)


@receiver(post_save, sender=models.NoticeMessage)
def notice_message(sender, **kwargs):
    serialize_model(sender)
