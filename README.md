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
    ./manage.py update_index
    ./manage.py runserver 0.0.0.0:8000

This will make the app accessible on the host machine as http://localhost:8111/ . The codebase is located on the host
machine, exported to the VM as a shared folder; code editing and Git operations will generally be done on the host.

Setup (without Vagrant)
-----

### Dependencies
* [PostgreSQL](http://www.postgresql.org)
* [Redis](http://redis.io/)
* [npm](https://npmjs.org/)
* [CoffeeScript](http://coffeescript.org/)
* [LESS](http://lesscss.org/)
* [Elasticsearch](http://www.elasticsearch.org/)
* [PIP](https://github.com/pypa/pip)

### Installation

With postgres, redis and elastisearch running, run the following commands:

	git clone https://github.com/torchbox/wagtaildemo.git
    cd wagtaildemo
    pip install -r requirements.txt
    ./manage.py createdb
    ./manage.py manage.py syncdb
    ./manage.py createsuperuser
    ./manage.py runserver

Hosted Elasticsearch
------

If you don't want to run an Elasticsearch server in development or production, there are many hosted services available, including Searchly, who offer a free account suitable for testing and development. To use Searchly:

* Sign up for an account at [dashboard.searchly.com/users/sign_up] (https://dashboard.searchly.com/users/sign_up)
* Use your Searchly dashboard to create a new index, e.g. 'wagtaildemo'
* Note the connection URL from your Searchly dashboard
* Update **WAGTAILSEARCH_BACKENDS** in your local settings

Example:

    WAGTAILSEARCH_BACKENDS = {
        'default': {
            'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
            'URLS': ['<url to elastic search here>'],
            'INDEX': '<index name here>',
        },
    }   

* Run **./manage.py update_index**