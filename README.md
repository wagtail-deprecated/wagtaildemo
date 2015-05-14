[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/torchbox/wagtaildemo)

Wagtail demo
=======================

This is a demonstration site implemented with [Wagtail CMS](http://wagtail.io).

To create your own site from scratch we strongly recommend the ``wagtail start`` command, explained in the [Wagtail CMS Documentation](http://wagtail.readthedocs.org/en/latest/getting_started/creating_your_project.html) however this demo provides some useful examples.

Setup with Vagrant (recommended)
-----

We recommend running Wagtail in a virtual machine using Vagrant, as this ensures that the correct dependencies are in place regardless of how your host machine is set up.

### Dependencies
* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant 1.5+](http://www.vagrantup.com)

### Installation
Run the following commands:

    git clone https://github.com/torchbox/wagtaildemo.git
    cd wagtaildemo
    vagrant up
    vagrant ssh
      (then, within the SSH session:)
    ./manage.py runserver 0.0.0.0:8000

The demo site will now be accessible at [http://localhost:8000/](http://localhost:8000/) and the Wagtail admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/) . Log into the admin with the credentials ``admin / changeme``.

Setup without Vagrant
-----
Don't want to set up a whole VM to try out Wagtail? No problem.

### Dependencies
* [PostgreSQL](http://www.postgresql.org)
* [PIP](https://github.com/pypa/pip)

### Installation

With PostgreSQL running (and configured to allow you to connect as the 'postgres' user - if not, you'll need to adjust the `createdb` line and the database settings in wagtaildemo/settings/base.py accordingly), run the following commands:

    git clone https://github.com/torchbox/wagtaildemo.git
    cd wagtaildemo
    pip install -r requirements/dev.txt
    createdb -Upostgres wagtaildemo
    ./manage.py migrate
    ./manage.py load_initial_data
    ./manage.py createsuperuser
    ./manage.py runserver

### SQLite support

SQLite is supported as an alternative to PostgreSQL - update the DATABASES setting
in wagtaildemo/settings/base.py to use 'django.db.backends.sqlite3', as you would
with a regular Django project.
