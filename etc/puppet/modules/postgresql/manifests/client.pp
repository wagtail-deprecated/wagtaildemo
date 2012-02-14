class postgresql::client {
  package { "postgresql-client":
    ensure => present,
  }
}
