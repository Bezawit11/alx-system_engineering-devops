# puppet file to fix  500 internal server error
exec { 'fixed_false':
  command => "sed -i 's/false/true/' /var/www/html/wp-config.php",
  path    => '/bin';
}
