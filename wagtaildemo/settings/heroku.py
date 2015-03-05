from .base import *
import os

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# BASE_URL required for notification emails
BASE_URL = 'http://localhost:8000'

import dj_database_url
DATABASES['default'] = dj_database_url.config()
DATABASES = {'default': dj_database_url.config(default='postgres://postgres@localhost:5432/wagtaildemo')}


try:
    from .local import *
except ImportError:
    pass
