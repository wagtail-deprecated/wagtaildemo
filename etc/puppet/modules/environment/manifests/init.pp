class environment ($virtualenv_name) {
	file { "bashrc":
		path => "/home/vagrant/.bashrc",
		ensure => present,
		owner => vagrant,
		group => vagrant,
		mode => 755,
		content => template('environment/bashrc.erb')
	}
}
