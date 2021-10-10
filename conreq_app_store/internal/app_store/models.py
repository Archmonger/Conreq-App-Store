import uuid

from django.db import models
from model_utils import FieldTracker
from multiselectfield import MultiSelectField
from versionfield import VersionField


# Create your models here.
class DevelopmentStage(models.TextChoices):
    PLANNING = "1 - Planning", "Planning"
    PREALPHA = "2 - Pre-Alpha", "Pre-Alpha"
    ALPHA = "3 - Alpha", "Alpha"
    BETA = "4 - Beta", "Beta"
    STABLE = "5 - Production/Stable", "Stable"
    MATURE = "6 - Mature", "Mature"
    INACTIVE = "7 - Inactive", "Inactive"


class AsyncCompatibility(models.TextChoices):
    NONE = "NONE", "No Async"
    SEMI = "SEMI", "Semi Async"
    FULL = "FULL", "Fully Async"


class SysPlatforms(models.TextChoices):
    AIX = "AIX", "Aix"
    LINUX = "LINUX", "Linux"
    WINDOWS = "WINDOWS", "Windows"
    CYGWIN = "CYGWIN", "Cygwin"
    MACOS = "MACOS", "Darwin"


class DescriptionTypes(models.TextChoices):
    PLAIN = "text/plain", "Plain Text (.txt)"
    RST = "text/x-rst", "reStructuredText (.rst)"
    MARKDOWN = "text/markdown", "Markdown (.md)"


class LicenseTypes(models.TextChoices):
    GPL3 = "GPL3", "GNU GPL v3"
    MIT = "MIT", "MIT License"
    APACHE2 = "APACHE2", "Apache License 2.0"
    BSD2 = "BSD2", "BSD 2-Clause Simplified License"
    BSD3 = "BSD3", "BSD 3-Clause Revised License"
    ECLIPSE2 = "ECLIPSE2", "Eclipse Public License 2.0"
    AGPL3 = "AGPL3", "GNU AGPL v3"
    GPL2 = "GPL2", "GNU GPL v2"
    LGPL2_1 = "LGPL2_1", "GNU LGPL v2.1"
    LGPL3 = "LGPL3", "GNU LGPL v3"
    MOZ2 = "MOZ2", "Mozilla Public License 2.0"
    UNLICENSE = "UNLICENSE", "The Unlicense"
    OTHER = "OTHER", "Other"


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


class AppPackage(models.Model):
    def __str__(self):
        return self.name

    # Unique Identifier
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Basic Info
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    long_description = models.FileField(upload_to="app_store/readme/")
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
    license_type = models.CharField(
        max_length=20,
        choices=LicenseTypes.choices,
        default=LicenseTypes.GPL3,
    )

    # Compatibility
    sys_platforms = MultiSelectField(choices=SysPlatforms.choices, max_length=10)
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
    required_app_packages = models.ManyToManyField("self", blank=True)
    optional_app_packages = models.ManyToManyField("self", blank=True)
    incompatible_app_packages = models.ManyToManyField("self", blank=True)
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
    app_package = models.ForeignKey(AppPackage, on_delete=models.CASCADE)


class Screenshot(models.Model):
    def __str__(self):
        return self.title

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="app_store/screenshot/")
    app_package = models.ForeignKey(AppPackage, on_delete=models.CASCADE)


class NoticeMessage(models.Model):
    def __str__(self):
        return self.title

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    message = models.TextField()
    app_package = models.ForeignKey(AppPackage, on_delete=models.CASCADE)
