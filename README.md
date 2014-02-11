Wagtail demo
=======================


Setup (with Vagrant - recommended)
-----

### Dependencies
[Vagrant 1.1+](http://www.vagrantup.com)

### Installation
Run the following commands:

    git clone https://github.com/torchbox/wagtaildemo.git
    cd wagtaildemo
    vagrant up
    vagrant ssh
      (then, within the SSH session:)
    ./manage.py createsuperuser
    ./manage.py runserver 0.0.0.0:8000

This will make the app accessible on the host machine as http://localhost:8111/ . The codebase is located on the host
machine, exported to the VM as a shared folder; code editing and Git operations will generally be done on the host.

Setup (without Vagrant)
-----

### Dependencies
* [PostgreSQL](http://www.postgresql.org)
* [npm](https://npmjs.org/)
* [CoffeeScript](http://coffeescript.org/)
* [LESS](http://lesscss.org/)
* [PIP](https://github.com/pypa/pip)

### Installation

With postgres running, run the following commands:

    git clone https://github.com/torchbox/wagtaildemo.git
    cd wagtaildemo
    pip install -r requirements/dev.txt
    ./manage.py createdb
    ./manage.py syncdb
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver

### SQLite support

SQLite is supported as an alternative to PostgreSQL - update the DATABASES setting
in wagtaildemo/settings/base.py to use 'django.db.backends.sqlite3', as you would
with a regular Django project. However, due to [an issue with migrations](https://github.com/torchbox/wagtail/issues/24),
you will need to run the following in place of manage.py migrate:

    python manage.py migrate 0001 --all
    python manage.py migrate
