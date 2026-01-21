#!/bin/bash

# Gestion de l'autoindex (on/off)
sed -i "s/AUTOINDEX_REPLACE/$AUTOINDEX/g" /etc/nginx/sites-available/default

# Initialisation de MySQL (MariaDB)
service mariadb start

# Création de la base de données et de l'utilisateur
# Remplacez 'user_db' et 'password123' par vos variables
mysql -e "CREATE DATABASE IF NOT EXISTS wordpress_db;"
mysql -e "CREATE USER IF NOT EXISTS 'admin_user'@'localhost' IDENTIFIED BY 'password123';"
mysql -e "GRANT ALL PRIVILEGES ON *.* TO 'admin_user'@'localhost';"
mysql -e "FLUSH PRIVILEGES;"

# Lancement de Supervisord (qui garde le conteneur ouvert et gère les services)
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf