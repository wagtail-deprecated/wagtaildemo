vagrant-django-template
=======================

A template for new Django 1.4 projects developed under Vagrant. Features offered include:

* A Vagrantfile for building an Ubuntu Lucid based VM
* A virtualenv (configured to be active on login), with project dependencies managed through a requirements.txt file
* A PostgreSQL database (with the same name as the project, pre-configured in the project settings file)
* South migrations
* Separation of configuration settings into base.py, dev.py and production.py (and optionally local.py, kept outside
  of version control) as per http://www.sparklewise.com/django-settings-for-production-and-development-best-practices/

Setup
-----
Install Django 1.4 on your host machine. (Be sure to explicitly uninstall earlier versions first, or use a virtualenv -
having earlier versions around seems to cause pre-1.4-style settings.py and urls.py files to be generated alongside the
new ones.) Check out the vagrant-django-template repository to some known location.

*Note to users outside Torchbox:* The Vagrantfile references http://vmimages.torchbox.com/django-base.box, an
internal-only URL to a prebuilt Vagrant box built according to https://github.com/torchbox/vagrant-django-base . You
should either build and host this yourself, or simply use http://files.vagrantup.com/lucid32.box instead (all of the
build scripts for getting from lucid32 to django-base are bundled in this project too).

To start a new project, run the following commands (from the place where you would usually create projects - not within
the vagrant-django-template checkout), changing /path/to/vagrant-django-template and myproject as appropriate:

    django-admin.py startproject --template /path/to/vagrant-django-template --name=Vagrantfile,machine.pp myproject
    cd myproject
    vagrant up
    vagrant ssh
      (then, within the SSH session:)
    ./manage.py runserver 0.0.0.0:8000

This will make the app accessible on the host machine as http://localhost:8111/ . The codebase is located on the host
machine, exported to the VM as a shared folder; code editing and Git operations will generally be done on the host.