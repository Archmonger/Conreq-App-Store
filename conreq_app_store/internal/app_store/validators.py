import os
from django.core.exceptions import ValidationError


def readme_extension_validator(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = {".rst", ".txt", ".md"}
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            f"Unsupported file extension. Must be one of the following: {valid_extensions}"
        )
