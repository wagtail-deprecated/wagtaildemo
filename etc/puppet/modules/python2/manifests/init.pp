class python2 {
	$packages = [
			"build-essential",
			"python",
			"python-dev",
			"python-setuptools",
	]

	package {
		$packages: ensure => installed;
	}

	exec { "install-virtualenvwrapper":
		path        => "/usr/local/bin:/usr/bin:/bin",
		refreshonly => true,
		command     => "easy_install virtualenvwrapper",
		require     => Package["python-setuptools"],
		subscribe   => Package["python-setuptools"],
	}
}
