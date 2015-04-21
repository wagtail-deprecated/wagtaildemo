from whitenoise.django import DjangoWhiteNoise

from .wsgi import application


application = DjangoWhiteNoise(application)
