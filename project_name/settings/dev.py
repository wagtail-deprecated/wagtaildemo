from .base import *

DEBUG = True
INSTALLED_APPS = list(INSTALLED_APPS) + ['devserver']

try:
	from .local import *
except ImportError:
	pass
