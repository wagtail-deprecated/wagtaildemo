$project_name = "myproject"

$database_name = $project_name
$virtualenv_name = $project_name

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
include environment

class {'virtualenv':
	virtualenv_name => $virtualenv_name
}

postgresql::database { $database_name:
	owner => "postgres",
}

exec {'pip-install-requirements':
	command => "pip install -E /home/vagrant/.virtualenvs/$virtualenv_name -r /home/vagrant/project/requirements.txt",
	user => vagrant,
}
