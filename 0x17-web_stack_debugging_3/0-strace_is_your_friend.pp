# puppet file to fix  500 internal server error
exec { 'fixed_false':
  command => "sed -i 's/define('WP_DEBUG', false);/define('WP_DEBUG', true);/' /var/www/html/wp-config.php",
  path    => '/bin';
}
