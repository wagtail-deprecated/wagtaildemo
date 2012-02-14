class postgresql::ruby {
  package { "libpgsql-ruby":
    ensure => present,
  }
}
