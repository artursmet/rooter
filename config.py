import logging
import os

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

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)


# Some Constants

NGINX_CONFIG_DIR="/etc/nginx/sites-available"
NGINX_ENABLED_DIR="/etc/nginx/sites-enabled"
APACHE_CONFIG_DIR="/etc/apache2/sites-available"
APACHE_ENABLED_DIR="/etc/apache2/sites-enabled"
TEMPLATE_DIR=rel("templates")
SUPERVISOR_DIR="/etc/supervisor/conf.d"
APP_DIR="/srv/django/"
from env import *
