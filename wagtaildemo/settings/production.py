from .base import *

DEBUG = False


WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
        'INDEX': 'wagtaildemo'
    }
}


INSTALLED_APPS+= (
    'djcelery',
    'kombu.transport.django',
    'gunicorn',    
)


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }
    }
}


# CELERY SETTINGS
import djcelery
djcelery.setup_loader()

BROKER_URL = 'redis://'
CELERY_SEND_TASK_ERROR_EMAILS = True
CELERYD_LOG_COLOR = False


try:
	from .local import *
except ImportError:
	pass
