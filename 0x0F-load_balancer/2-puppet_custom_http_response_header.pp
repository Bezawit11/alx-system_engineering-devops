# Automation: creates a custom HTTP header response with Puppet.
exec { 'command':
  command  => 'sudo apt-get update;
  sudo apt-get -y install nginx;
  sudo service nginx start;
  sudo sed -i "11i\\\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf;
  service nginx restart',
  provider => shell,
}
