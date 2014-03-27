#!/bin/bash

# Script to set up a Django project on Vagrant.

# Installation settings

PROJECT_NAME=$1

DB_NAME=$PROJECT_NAME
VIRTUALENV_NAME=$PROJECT_NAME

PROJECT_DIR=/home/vagrant/$PROJECT_NAME
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME

PGSQL_VERSION=9.1

# Need to fix locale so that Postgres creates databases in UTF-8
cp -p $PROJECT_DIR/etc/install/etc-bash.bashrc /etc/bash.bashrc
locale-gen en_GB.UTF-8
dpkg-reconfigure locales

export LANGUAGE=en_GB.UTF-8
export LANG=en_GB.UTF-8
export LC_ALL=en_GB.UTF-8

# Install essential packages from Apt
apt-get update -y
# Python dev packages
apt-get install -y build-essential python3 python3-dev python3-setuptools
# Dependencies for image processing with Pillow (drop-in replacement for PIL)
# supporting: jpeg, tiff, png, freetype, littlecms
# (pip install pillow to get pillow itself)
apt-get install -y libjpeg-dev libtiff-dev zlib1g-dev libfreetype6-dev liblcms2-dev
# Git (we'd rather avoid people keeping credentials for git commits in the repo, but sometimes we need it for pip requirements that aren't in PyPI)
apt-get install -y git

# Optional: install redis (recommended for production sites as a backend
# for Celery and Django cache)
#
# apt-get install -y redis-server

# Postgresql
if ! command -v psql; then
    apt-get install -y postgresql-$PGSQL_VERSION libpq-dev
    cp $PROJECT_DIR/etc/install/pg_hba.conf /etc/postgresql/$PGSQL_VERSION/main/
    /etc/init.d/postgresql reload
fi

# virtualenv global setup
easy_install3 -U pip

# Need to install PBR from github repo as version in pypi doesn't work on Python <3.3
# https://github.com/openstack-dev/pbr/pull/5
pip install -e git+https://github.com/openstack-dev/pbr.git@95c86cbed7b10ae7385b0b894600c763decd2558#egg=pbr
pip install virtualenv virtualenvwrapper stevedore virtualenv-clone


# bash environment global setup
cp -p $PROJECT_DIR/etc/install/bashrc /home/vagrant/.bashrc
su - vagrant -c "mkdir -p /home/vagrant/.pip_download_cache"

# ---

# Optional: install ElasticSearch (for higher-performance / more flexible search functionality)
#
# if ! command -v /usr/share/elasticsearch/bin/elasticsearch; then
#     apt-get install -y openjdk-6-jre-headless
#     echo "Downloading ElasticSearch..."
#     wget -q https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.11.deb
#     dpkg -i elasticsearch-0.90.11.deb
#     service elasticsearch start
# fi

# postgresql setup for project
createdb -Upostgres $DB_NAME

# dependencies for lxml (for HTML whitelisting)
apt-get install -y libxml2-dev libxslt-dev

# virtualenv setup for project
su - vagrant -c "/usr/local/bin/virtualenv $VIRTUALENV_DIR && \
    echo $PROJECT_DIR > $VIRTUALENV_DIR/.project && \
    PIP_DOWNLOAD_CACHE=/home/vagrant/.pip_download_cache $VIRTUALENV_DIR/bin/pip install -r $PROJECT_DIR/requirements/dev.txt"

echo "workon $VIRTUALENV_NAME" >> /home/vagrant/.bashrc

# Set execute permissions on manage.py, as they get lost if we build from a zip file
chmod a+x $PROJECT_DIR/manage.py

# Django project setup
su - vagrant -c "source $VIRTUALENV_DIR/bin/activate && cd $PROJECT_DIR && python manage.py syncdb --noinput && python manage.py migrate --noinput"
