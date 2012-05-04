$project_name = "{{ project_name }}"

$database_name = $project_name
$virtualenv_name = $project_name

$project_dir = "/home/vagrant/$project_name"
$virtualenv_dir = "/home/vagrant/.virtualenvs/$project_name"

# http://groups.google.com/group/vagrant-up/browse_thread/thread/0fbd824efcce973f
group { "puppet":
	ensure => "present",
}

# http://groups.google.com/group/puppet-users/browse_thread/thread/c60e8ae314ae687b
Exec {
	path => ["/bin", "/sbin", "/usr/bin", "/usr/sbin"],
}

# Ensure apt-get update has been run before installing any packages
# http://mig5.net/node/347 , http://johnleach.co.uk/words/771/puppet-dependencies-and-run-stages
exec { "apt-update":
	command => "/usr/bin/apt-get update"
}
Exec["apt-update"] -> Package <| |>

include python2
include postgresql::server

class {'environment':
	virtualenv_name => $virtualenv_name
}

class {'virtualenv':
	virtualenv_name => $virtualenv_name,
	project_dir => $project_dir,
}

postgresql::database { $database_name:
	owner => "postgres",
}

exec {'pip-install-requirements':
	command => "pip install -E $virtualenv_dir -r $project_dir/requirements.txt",
	user => vagrant,
	path => "/usr/local/bin:/usr/bin:/bin",
	require => Class["python2"],
}

exec {'django-db-setup':
	command => "/bin/bash -c 'source $virtualenv_dir/bin/activate && cd $project_dir && ./manage.py syncdb --noinput && ./manage.py migrate'",
	user => vagrant,
	require => [ Exec["pip-install-requirements"], Postgresql::Database[$database_name] ],
}
