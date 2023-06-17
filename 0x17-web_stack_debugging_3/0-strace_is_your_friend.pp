# This attempts to solve the debugging part of web 3 like who names a php file .phpp
exec {'fix-php':
  command  => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  provider => 'shell',
}
