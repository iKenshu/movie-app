from .base import *
from .base import env

DEBUG = True

ALLOW_HOSTS = ["127.0.0.1", "0.0.0.0", "localhost"]

INSTALLED_APPS += ("django_extensions", "debug_toolbar")

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
