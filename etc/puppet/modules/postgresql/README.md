Puppet PostgreSQL Module
========================

Module for configuring PostgreSQL.

Tested on Debian GNU/Linux 6.0 Squeeze and Ubuntu 10.4 LTS with
Puppet 2.6. Patches for other operating systems welcome.


TODO
----

* Ability to configure authentication settings.


Installation
------------

Clone this repo to a postgresql directory under your Puppet
modules directory:

    git clone git://github.com/uggedal/puppet-module-postgresql.git postgresql

If you don't have a Puppet Master you can create a manifest file
based on the notes below and run Puppet in stand-alone mode
providing the module directory you cloned this repo to:

    puppet apply --modulepath=modules test_postgresql.pp


Usage
-----

To install and configure PostgreSQL, include the module:

    include postgresql::server

You can override defaults in the PostgreSQL config by including
the module with this special syntax:

    class { "postgresql::server": version => "8.4",
                        listen_addresses => 'localhost',
                        max_connections => 100,
                        shared_buffers => '24MB',
    }

If you need language specific PostgreSQL modules include their class:

    include postgresql::python
    include postgresql::ruby

Creating a database is done with the `postgresql::database` resource. If
the owner does not exist it is created:

    postgresql::database { "blog":
      owner => "bloguser",
    }

Note that you'll need to define a global search path for the `exec`
resource to make the `postgresql::database` resource function
properly. This should ideally be placed in `manifests/site.pp`:

    Exec {
      path => "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    }
