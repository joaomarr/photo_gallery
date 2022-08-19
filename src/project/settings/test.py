# flake8: noqa

from .base import *

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"},
}

MIGRATION_MODULES = {
    "auth": None,
    "admin": None,
    "contenttypes": None,
    "sessions": None,
}
