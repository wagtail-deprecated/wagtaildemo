FROM python:2.7

# Install requirements first (so they get cached between builds)
ADD requirements requirements
RUN pip install -r requirements/docker.txt

# Add code into container
ADD . /app/
WORKDIR /app/

ENV PYTHONPATH=/app/
ENV DJANGO_SETTINGS_MODULE=wagtaildemo.settings.production
