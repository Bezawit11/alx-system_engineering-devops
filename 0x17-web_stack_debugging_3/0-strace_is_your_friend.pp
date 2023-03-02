# puppet file to fix  500 internal server erro
exec { 'fixed-config':
  command => "sed -i 's/define("WP_DEBUG", true);/define("WP_DEBUG", false);/g' /var/www/html/wp-config.php",
  path    => '/bin';
}
