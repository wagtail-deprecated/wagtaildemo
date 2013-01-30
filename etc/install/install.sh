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
apt-get install -y build-essential python python-dev python-setuptools python-pip postgresql-$PGSQL_VERSION libpq-dev

# postgresql setup
cp $PROJECT_DIR/etc/install/pg_hba.conf /etc/postgresql/$PGSQL_VERSION/main/
/etc/init.d/postgresql reload
createdb -Upostgres $DB_NAME

# virtualenv setup
easy_install virtualenv virtualenvwrapper stevedore virtualenv-clone
sudo -u vagrant -s -- /usr/local/bin/virtualenv $VIRTUALENV_DIR
sudo -u vagrant -s -- echo $PROJECT_DIR > $VIRTUALENV_DIR/.project

cp -p $PROJECT_DIR/etc/install/bashrc /home/vagrant/.bashrc
echo "workon $VIRTUALENV_NAME" >> /home/vagrant/.bashrc
sudo -u vagrant -s -- /usr/bin/pip install -E $VIRTUALENV_DIR -r $PROJECT_DIR/requirements.txt

# Set execute permissions on manage.py, as they get lost if we build from a zip file
chmod a+x $PROJECT_DIR/manage.py

# Django project setup
su - vagrant -c "source $VIRTUALENV_DIR/bin/activate && cd $PROJECT_DIR && ./manage.py syncdb --noinput && ./manage.py migrate"
