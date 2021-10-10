from django.db import models


class DevelopmentStage(models.TextChoices):
    PLANNING = "1 - Planning", "Planning"
    PREALPHA = "2 - Pre-Alpha", "Pre-Alpha"
    ALPHA = "3 - Alpha", "Alpha"
    BETA = "4 - Beta", "Beta"
    STABLE = "5 - Production/Stable", "Stable"
    MATURE = "6 - Mature", "Mature"
    INACTIVE = "7 - Inactive", "Inactive"


class AsyncCompatibility(models.TextChoices):
    NONE = "NONE", "Not Async"
    SEMI = "SEMI", "Partially Async"
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
