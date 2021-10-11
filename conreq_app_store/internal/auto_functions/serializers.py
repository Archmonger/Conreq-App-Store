from django.conf import settings
from django.core.serializers import serialize
from django.db.models.signals import post_save
from django.dispatch import receiver

from ..app_store import models

MODELS_DIR = getattr(settings, "MODELS_DIR")

# pylint: disable=unused-argument,missing-function-docstring


def write_json(model):
    data = serialize("json", model.objects.all())
    with open(MODELS_DIR / f"{model.__name__}.json", "w", encoding="utf-8") as fp:
        fp.write(data)


@receiver(post_save, sender=models.Category)
def serialize_category(sender, **kwargs):
    write_json(sender)


@receiver(post_save, sender=models.Subcategory)
def serialize_subcategory(sender, **kwargs):
    write_json(sender)


@receiver(post_save, sender=models.ConreqPackage)
def serialize_conreq_package(sender, **kwargs):
    write_json(sender)


@receiver(post_save, sender=models.EnvironmentVariable)
def serialize_enviroment_variables(sender, **kwargs):
    write_json(sender)


@receiver(post_save, sender=models.Screenshot)
def serialize_screenshot(sender, **kwargs):
    write_json(sender)


@receiver(post_save, sender=models.NoticeMessage)
def serialize_notice_message(sender, **kwargs):
    write_json(sender)
