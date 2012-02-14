class postgresql::server($version="8.4",
                         $listen_addresses='localhost',
                         $max_connections=100,
                         $shared_buffers='24MB') {
  include postgresql::client

  $service_name = $operatingsystem ? {
    "Ubuntu" => "postgresql-${version}",
    default => "postgresql",
  }

  package { postgresql:
    ensure => present,
  }

  File {
    owner => "postgres",
    group => "postgres",
  }

  file { "pg_hba.conf":
    path => "/etc/postgresql/${version}/main/pg_hba.conf",
    source => "puppet:///modules/postgresql/pg_hba.conf",
    mode => 640,
    require => Package[postgresql],
  }

  file { "postgresql.conf":
    path => "/etc/postgresql/${version}/main/postgresql.conf",
    content => template("postgresql/postgresql.conf.erb"),
    require => Package[postgresql],
  }

  service { $service_name:
    ensure => running,
    enable => true,
    hasstatus => true,
    hasrestart => true,
    subscribe => [Package["postgresql"],
                  File["pg_hba.conf"],
                  File["postgresql.conf"]],
  }
}
