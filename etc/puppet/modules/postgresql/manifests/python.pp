class postgresql::python {
  package { "python-psycopg2":
    ensure => present,
  }
}

