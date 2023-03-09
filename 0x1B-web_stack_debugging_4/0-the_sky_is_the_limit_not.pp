# puppet file to fix  500 internal server error
exec { 'fixed-phpp':
  command => sed '4 a worker_rlimit_nofile 30000;' /etc/nginx/nginx.conf
  path    => '/bin';
}
