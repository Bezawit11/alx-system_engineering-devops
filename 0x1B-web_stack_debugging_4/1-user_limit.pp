# puppet file to fix  500 internal server error
exec { 'fixed-login':
  command => useradd holberton;
  path    => '/bin';
}
