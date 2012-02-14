define postgresql::user($ensure=present) {
  $userexists = "psql --tuples-only -c 'SELECT rolname FROM pg_catalog.pg_roles;' | grep '^ ${owner}$'"
  $user_owns_zero_databases = "psql --tuples-only --no-align -c \"SELECT COUNT(*) FROM pg_catalog.pg_database JOIN pg_authid ON pg_catalog.pg_database.datdba = pg_authid.oid WHERE rolname = '${owner}';\" | grep -e '^0$'"

  if $ensure == 'present' {

    exec { "createuser $owner":
      command => "createuser --no-superuser --no-createdb --no-createrole ${owner}",
      user    => "postgres",
      unless  => $userexists,
      require => Class["postgresql::server"],
    }

  } elsif $ensure == 'absent' {

    exec { "dropuser $owner":
      command => "dropuser ${owner}",
      user => "postgres",
      onlyif => "$userexists && $user_owns_zero_databases",
    }
  }
}
