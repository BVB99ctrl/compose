FROM debian:bullseye

# Installation des dépendances
RUN apt-get update && apt-get install -y \
    nginx \
    mariadb-server \
    php-fpm \
    php-mysql \
    php-mbstring \
    supervisor \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*
    # Crée le dossier pour la socket PHP et donne les droits à Nginx
RUN mkdir -p /run/php && chown -R www-data:www-data /run/php

# Configuration de WordPress
RUN wget https://wordpress.org/latest.tar.gz && \
    tar -xvf latest.tar.gz -C /var/www/html/ && \
    rm latest.tar.gz

# Configuration de phpMyAdmin
RUN wget https://files.phpmyadmin.net/phpMyAdmin/5.2.1/phpMyAdmin-5.2.1-all-languages.zip && \
    unzip phpMyAdmin-5.2.1-all-languages.zip && \
    mv phpMyAdmin-5.2.1-all-languages /var/www/html/phpmyadmin && \
    rm phpMyAdmin-5.2.1-all-languages.zip
    

# Copie des configurations
COPY ./default.conf /etc/nginx/sites-available/default
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY setup.sh /usr/local/bin/setup.sh

RUN chmod +x /usr/local/bin/setup.sh && sed -i 's/\r$//' /usr/local/bin/setup.sh

# Variable d'environnement par défaut pour l'autoindex
ENV AUTOINDEX=on

EXPOSE 80

ENTRYPOINT ["/bin/bash", "/usr/local/bin/setup.sh"]