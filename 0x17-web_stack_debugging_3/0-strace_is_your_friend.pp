# puppet file to fix  500 internal server error
exec { 'fixed_false':
  command => "sed -i 's/('WP_DEBUG', false);/('WP_DEBUG', true);/' /var/www/html/wp-config.php",
  path    => '/bin';
}
