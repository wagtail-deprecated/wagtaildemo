class virtualenv ($virtualenv_name) {
	include python2
	
	$virtualenv_path = "/home/vagrant/.virtualenv/${virtualenv_name}"
	exec {"mkvirtualenv $virtualenv_name":
		command => "/usr/local/bin/virtualenv --no-site-packages $virtualenv_path",
		user => vagrant,
		creates => $virtualenv_path
	}
}
