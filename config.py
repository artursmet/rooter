import logging

DEBUG = True

if DEBUG:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%b %d %Y %H:%M:%S'
    )
else:
    logging.basicConfig(
        filename='error_log.log',
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%b %d %Y %H:%M:%S'
    )


# Some Constants

NGINX_CONFIG_DIR="/etc/nginx/sites-available"
NGINX_ENABLED_DIR="/etc/nginx/sites-enabled"
APACHE_CONFIG_DIR="/etc/apache2/sites-available"
APACHE_ENABLED_DIR="/etc/apache2/sites-enabled"
TEMPLATE_DIR="templates"
SUPERVISOR_DIR="/etc/supervisor/conf.d"

from env import *
