#!/usr/bin/env python
#coding: utf-8

from config import *
from utils import get_template
import subprocess


def add_proxy_vhost(domain_name):
    config = get_template("nginx_proxy.conf")
    ready_config = config.render(domain=domain_name)
    logging.debug("Config with domain_name %s rendered." % domain_name)
    logging.debug("Writing config into new file")
    dest_file_path = "%s/%s.conf" % (NGINX_CONFIG_DIR, domain_name)
    try:
        dest_file = open(dest_file_path, 'w')
        dest_file.write(ready_config)
        dest_file.close()
    except IOError, exc:
        logging.error("I/O Error. %s" % exc)
        raise

    logging.debug("Config written to file %s" % dest_file_path)

def enable_vhost(domain_name):
    logging.debug("Enabling vhost %s" % domain_name)
    enabled_path = "%s/%s.conf" % (NGINX_ENABLED_DIR, domain_name)
    available_path = "%s/%s.conf" % (NGINX_CONFIG_DIR, domain_name)
    result = subprocess.call("ln -s %s %s" % (enabled_path, available_path))
    logging.debug("Symlink creation end with code %s" % result)

def disable_vhost(domain_name):
    logging.debug("Disabling vhost %s" % domain_name)
    enabled_path = "%s/%s.conf" % (NGINX_ENABLED_DIR, domain_name)
    result = subprocess.call("rm %s" % enabled_path)
    logging.debug("Symlink deletion end with code %s" % result)

def delete_vhost(domain_name):
    logging.debug("Deleting vhost %s" % domain_name)
    available_path = "%s/%s.conf" % (NGINX_CONFIG_DIR, domain_name)
    result = subprocess.call("rm %s" % available_path)
    logging.debug("Config deletion end with code %s" % result)
