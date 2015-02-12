[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/torchbox/wagtaildemo)

Wagtail demo
=======================

[Wagtail](http://wagtail.io) is distributed as a Python package, to be incorporated into a Django project via the INSTALLED_APPS setting. To get you up and running quickly, we provide a demo site with all the configuration in place, including a set of example page types.

Setup (with Vagrant - recommended)
-----

We recommend running Wagtail in a virtual machine using Vagrant, as this ensures that the correct dependencies are in place regardless of how your host machine is set up.

### Dependencies
* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant 1.1+](http://www.vagrantup.com)

### Installation
Run the following commands:

    git clone https://github.com/torchbox/wagtaildemo.git
    cd wagtaildemo
    vagrant up
    vagrant ssh
      (then, within the SSH session:)
    ./manage.py runserver 0.0.0.0:8000

This will make the app accessible on the host machine as http://localhost:8000/ - you can access the Wagtail admin interface at http://localhost:8000/admin/ . The codebase is located on the host
machine, exported to the VM as a shared folder; code editing and Git operations will generally be done on the host. A superuser with the credentials ``admin / changeme`` is automatically created.

### Developing Wagtail
The above setup is all you need for trying out the demo site and building Wagtail-powered sites. To develop Wagtail itself, you'll need a working copy of [the Wagtail codebase](https://github.com/torchbox/wagtail) alongside your demo site, shared with your VM so that it is picked up instead of the packaged copy of Wagtail. From the location where you cloned wagtaildemo:

    git clone https://github.com/torchbox/wagtail.git
    cd wagtaildemo
    cp Vagrantfile.local.example Vagrantfile.local
        (edit Vagrantfile.local to specify the path to the wagtail codebase, if required)
    cp wagtaildemo/settings/local.py.example wagtaildemo/settings/local.py
        (uncomment the lines from 'import sys' onward, and edit the rest of local.py as appropriate)

If your VM is currently running, you'll then need to run `vagrant halt` followed by `vagrant up` for the changes to take effect.

Setup (without Vagrant)
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

Upgrade from Django 1.6
-----
If you checked out a copy of wagtaildemo prior to 5th January 2015, it will be running under Django 1.6. To upgrade to Django 1.7 while preserving existing data, perform the following steps:

(outside of Vagrant)

    git pull
    git checkout pre-django1.7

if you have set up your wagtaildemo instance to track the wagtail git repo (as described in "Developing Wagtail" above), you should also check out the 'stable/0.8.x' branch of wagtail at this point.

(within Vagrant)

    pip install -r requirements/dev.txt
    ./manage.py migrate

(outside Vagrant)

    git checkout master

(within Vagrant)

    pip install -r requirements/dev.txt
    ./manage.py migrate --fake
