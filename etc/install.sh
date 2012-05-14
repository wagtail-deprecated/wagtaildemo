#!/bin/bash

# Script to set up a Django project on Vagrant.

# Installation settings

PROJECT_NAME=$1

DB_NAME=$PROJECT_NAME
VIRTUALENV_NAME=$PROJECT_NAME

PROJECT_DIR=/home/vagrant/$PROJECT_NAME
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME

# Install essential packages from Apt
apt-get update -y
apt-get install -y build-essential python python-dev python-setuptools python-pip postgresql libpq-dev

# virtualenv setup
easy_install virtualenvwrapper
sudo -u vagrant -s -- /usr/local/bin/virtualenv $VIRTUALENV_DIR
sudo -u vagrant -s -- echo $PROJECT_DIR > $VIRTUALENV_DIR/.project

cp -p $PROJECT_DIR/etc/bashrc /home/vagrant/.bashrc
echo "workon $VIRTUALENV_NAME" >> /home/vagrant/.bashrc
sudo -u vagrant -s -- /usr/bin/pip install -E $VIRTUALENV_DIR -r $PROJECT_DIR/requirements.txt
