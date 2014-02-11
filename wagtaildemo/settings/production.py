from .base import *

DEBUG = False

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
        'INDEX': 'wagtaildemo'
    }
}

try:
	from .local import *
except ImportError:
	pass
