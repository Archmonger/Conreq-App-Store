from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Category)
class AppCategories(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(models.Subcategory)
class AppSubCategories(admin.ModelAdmin):
    list_display = ["name", "category"]
    search_fields = ["name", "category"]
    list_filter = ["name", "category"]


@admin.register(models.ConreqPackage)
class Apps(admin.ModelAdmin):
    list_display = ["name", "development_stage", "author_name"]
    list_editable = ["development_stage"]
    search_fields = [
        "name",
        "short_description",
        "long_description",
        "subcategories",
        "author_name",
        "author_email",
        "author_url",
        "repository_url",
        "homepage_url",
        "support_url",
        "donation_url",
        "pypi_url",
        "system_platforms",
        "required_conreq_packages",
        "optional_conreq_packages",
    ]
    list_filter = [
        "author_name",
        "system_platforms",
        "desktop_compatible",
        "touch_compatible",
        "mobile_compatible",
        "required_conreq_packages",
        "optional_conreq_packages",
        "incompatible_conreq_packages",
        "incompatible_categories",
        "incompatible_subcategories",
    ]


@admin.register(models.EnvironmentVariable)
class EnvironmentVariables(admin.ModelAdmin):
    list_display = ["uuid", "name", "default_value", "required", "conreq_package"]
    list_editable = ["name", "default_value"]
    search_fields = ["name", "default_value", "example_values", "conreq_package"]
    list_filter = ["conreq_package"]


@admin.register(models.Screenshot)
class Screenshots(admin.ModelAdmin):
    list_display = ["title", "conreq_package"]
    search_fields = ["title", "description", "conreq_package"]
    list_filter = ["conreq_package"]


@admin.register(models.NoticeMessage)
class NoticeMessages(admin.ModelAdmin):
    list_display = ["title", "conreq_package"]
    search_fields = ["title", "message", "conreq_package"]
    list_filter = ["conreq_package"]
