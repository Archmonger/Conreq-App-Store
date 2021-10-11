from django.conf import settings
from django.core.serializers import deserialize

from ..app_store import models

MODELS_DIR = getattr(settings, "MODELS_DIR")
MODELS = [
    models.Category,
    models.Subcategory,
    models.ConreqPackage,
    models.EnvironmentVariable,
    models.Screenshot,
    models.NoticeMessage,
]


def deserialize_model(model):
    json_path = MODELS_DIR / f"{model.__name__}.json"
    if not json_path.exists():
        print(f"{json_path} does not exist!")
        return
    with open(json_path, "r", encoding="utf-8") as fp:
        for db_entry in deserialize("json", fp):
            db_entry.save()


def deserialize_all():
    for model in MODELS:
        deserialize_model(model)
