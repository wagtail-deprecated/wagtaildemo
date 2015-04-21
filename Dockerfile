FROM python:2.7

# Install requirements first (so they get cached between builds)
ADD requirements requirements
RUN pip install -r requirements/docker.txt

# Add code into container
ADD . /app/
WORKDIR /app/

# Environment variables
ENV PYTHONPATH=/app/
ENV DJANGO_SETTINGS_MODULE=wagtaildemo.settings.docker

# Create database
RUN django-admin.py migrate --noinput
RUN django-admin.py load_initial_data

# Compress static files
RUN django-admin.py collectstatic --noinput
RUN django-admin.py compress
RUN python -m whitenoise.gzip /app/static/

CMD uwsgi --ini uwsgi.ini
EXPOSE 80
