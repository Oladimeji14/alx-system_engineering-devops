exec { 'fix_typo_in_php_files':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => "sed -i 's/\.phpp/\.php/g' /var/www/html/wp-settings.php",
  onlyif  => "grep -q '\.phpp' /var/www/html/wp-settings.php",
}
