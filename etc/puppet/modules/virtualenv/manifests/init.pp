class virtualenv ($virtualenv_name, $project_dir=undef) {
	include python2
	
	$virtualenv_path = "/home/vagrant/.virtualenvs/${virtualenv_name}"
	exec {"mkvirtualenv $virtualenv_name":
		command => "/usr/local/bin/virtualenv --no-site-packages $virtualenv_path",
		user => vagrant,
		creates => $virtualenv_path
	}

	if $project_dir {
		file { "$virtualenv_path/.project":
			ensure => present,
			content => $project_dir,
			require => Exec["mkvirtualenv $virtualenv_name"]
		}
	}
}
