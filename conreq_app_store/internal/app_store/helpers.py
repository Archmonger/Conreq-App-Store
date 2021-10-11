import os
import uuid


def readme_path(instance, filename):
    ext = filename.split(".")[-1]
    uuid_filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("app_store/readme", uuid_filename)


def screenshots_path(instance, filename):
    ext = filename.split(".")[-1]
    uuid_filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("app_store/screenshot", uuid_filename)
