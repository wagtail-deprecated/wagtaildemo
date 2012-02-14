class environment {
	file { "bashrc":
		path => "/home/vagrant/.bashrc",
		ensure => present,
		owner => vagrant,
		group => vagrant,
		mode => 755,
		source => "puppet:///modules/environment/bashrc"
	}
}
