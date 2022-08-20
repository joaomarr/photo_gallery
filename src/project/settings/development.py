from .base import *  # noqa
from decouple import config

DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": config("DB_NAME", os.path.join(BASE_DIR, "db.postgresql")),
        "USER": config("DB_USER", "user"),
        "PASSWORD": config("DB_PASSWORD", "password"),
        "HOST": config("DB_HOST", "localhost"),
        "PORT": config("DB_PORT", "5432"),
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
    'graphql_auth',
    'django_filters',
    'boto3',
    'authentication',
    'photo_gallery',
    'photos',
]

GRAPHQL_AUTH = {
 "REGISTER_MUTATION_FIELDS_OPTIONAL": ["first_name", "last_name", "username"],
 "REGISTER_MUTATION_FIELDS": ["email"],
 "SEND_ACTIVATION_EMAIL": False,
}

ALLOWED_HOSTS = ['*']

AWS_QUERYSTRING_AUTH = config("AWS_QUERYSTRING_AUTH")
AWS_DEFAULT_ACL = config("AWS_DEFAULT_ACL")

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACESS_KEY = config("AWS_SECRET_ACESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"