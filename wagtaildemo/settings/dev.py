from .base import *

DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# BASE_URL required for notification emails
BASE_URL = 'http://localhost:8000'

try:
    from .local import *
except ImportError:
    pass
