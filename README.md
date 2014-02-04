Wagtail demo
=======================

Setup
-----

Run the following commands:

    git clone https://github.com/torchbox/wagtaildemo.git
    cd wagtaildemo
    vagrant up
    vagrant ssh
      (then, within the SSH session:)
    ./manage.py runserver 0.0.0.0:8000

This will make the app accessible on the host machine as http://localhost:8111/ . The codebase is located on the host
machine, exported to the VM as a shared folder; code editing and Git operations will generally be done on the host.
