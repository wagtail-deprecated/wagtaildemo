#!/bin/bash

# Script to set up a Django project on Vagrant.

# Installation settings

PROJECT_NAME=$1

DB_NAME=$PROJECT_NAME
VIRTUALENV_NAME=$PROJECT_NAME

PROJECT_DIR=/home/vagrant/$PROJECT_NAME
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME

PGSQL_VERSION=8.4

# Install essential packages from Apt
apt-get update -y
apt-get install -y build-essential python python-dev python-setuptools python-pip postgresql-$PGSQL_VERSION libpq-dev

# postgresql setup
cp $PROJECT_DIR/etc/install/pg_hba.conf /etc/postgresql/$PGSQL_VERSION/main/
/etc/init.d/postgresql-$PGSQL_VERSION reload
createdb -Upostgres $DB_NAME

# virtualenv setup
easy_install virtualenv virtualenvwrapper
sudo -u vagrant -s -- /usr/local/bin/virtualenv $VIRTUALENV_DIR
sudo -u vagrant -s -- echo $PROJECT_DIR > $VIRTUALENV_DIR/.project

cp -p $PROJECT_DIR/etc/install/bashrc /home/vagrant/.bashrc
echo "workon $VIRTUALENV_NAME" >> /home/vagrant/.bashrc
sudo -u vagrant -s -- /usr/bin/pip install -E $VIRTUALENV_DIR -r $PROJECT_DIR/requirements.txt

# Set execute permissions on manage.py, as they get lost if we build from a zip file
chmod a+x $PROJECT_DIR/manage.py

# Django project setup
sudo -u vagrant -i -- "source $VIRTUALENV_DIR/bin/activate && cd $PROJECT_DIR && ./manage.py syncdb --noinput && ./manage.py migrate"
