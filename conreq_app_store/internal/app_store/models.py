import uuid

from django.db import models
from model_utils import FieldTracker
from multiselectfield import MultiSelectField
from versionfield import VersionField

from .choices import (
    AsyncCompatibility,
    DescriptionTypes,
    DevelopmentStage,
    LicenseTypes,
    SysPlatforms,
)
from .helpers import readme_path, screenshots_path
from .validators import readme_extension_validator

# TODO: Add on_save behavior to serialize this data into json


class Category(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    # Basic Info
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)

    # Tracker
    tracker = FieldTracker()


class Subcategory(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

    # Basic Info
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Tracker
    tracker = FieldTracker()


class ConreqPackage(models.Model):
    def __str__(self):
        return self.name

    # Unique Identifier
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Basic Info
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    long_description = models.FileField(
        upload_to=readme_path, validators=[readme_extension_validator]
    )
    long_description_type = models.CharField(
        max_length=20,
        choices=DescriptionTypes.choices,
        default=DescriptionTypes.MARKDOWN,
    )
    subcategories = models.ManyToManyField(Subcategory)
    development_stage = models.CharField(
        max_length=21,
        choices=DevelopmentStage.choices,
        default=DevelopmentStage.PREALPHA,
    )
    version = VersionField(default="0.0.1")
    banner_message = models.TextField(blank=True, null=True)

    # Ownership Info
    author = models.CharField(max_length=50)
    author_email = models.EmailField(blank=True, null=True)
    author_url = models.URLField(blank=True, null=True)
    repository_url = models.URLField()
    homepage_url = models.URLField(blank=True, null=True)
    support_url = models.URLField(blank=True, null=True)
    donation_url = models.URLField(blank=True, null=True)
    pypi_url = models.URLField(blank=True, null=True)
    license_url = models.URLField(blank=True, null=True)
    license_type = models.CharField(
        max_length=20,
        choices=LicenseTypes.choices,
        default=LicenseTypes.GPL3,
    )

    # Compatibility
    sys_platforms = MultiSelectField(choices=SysPlatforms.choices, max_length=50)
    desktop_compatible = models.BooleanField()
    touch_compatible = models.BooleanField()
    mobile_compatible = models.BooleanField()
    minimum_conreq_version = VersionField(default="0.0.1")
    tested_conreq_version = VersionField(default="1.0.0")
    max_conreq_version = VersionField(blank=True, null=True)
    asynchronous = models.CharField(
        max_length=20,
        choices=AsyncCompatibility.choices,
        default=AsyncCompatibility.NONE,
    )

    # App Dependencies
    required_conreq_packages = models.ManyToManyField("self", blank=True)
    optional_conreq_packages = models.ManyToManyField("self", blank=True)
    incompatible_conreq_packages = models.ManyToManyField("self", blank=True)
    incompatible_categories = models.ManyToManyField(
        Category, related_name="incompatible_categories", blank=True
    )
    incompatible_subcategories = models.ManyToManyField(
        Subcategory, related_name="incompatible_subcategories", blank=True
    )

    # Tracker
    tracker = FieldTracker()


class EnvironmentVariable(models.Model):
    def __str__(self):
        return self.name + ' = "' + str(self.default_value) + '"'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    required = models.BooleanField(default=False)
    default_value = models.CharField(max_length=255, blank=True, null=True)
    example_values = models.CharField(max_length=255, blank=True, null=True)
    conreq_package = models.ForeignKey(ConreqPackage, on_delete=models.CASCADE)


class Screenshot(models.Model):
    def __str__(self):
        return self.title

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=screenshots_path)
    conreq_package = models.ForeignKey(ConreqPackage, on_delete=models.CASCADE)


class NoticeMessage(models.Model):
    def __str__(self):
        return self.title

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    message = models.TextField()
    conreq_package = models.ForeignKey(ConreqPackage, on_delete=models.CASCADE)
