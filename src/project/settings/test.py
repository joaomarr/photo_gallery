# flake8: noqa

from .base import *

DATABASES = {
    "default": {"ENGINE": "django.db.backends.postgresql", "NAME": ":memory:"},
}

MIGRATION_MODULES = {
    "auth": None,
    "admin": None,
    "contenttypes": None,
    "sessions": None,
}
