#!/usr/bin/env python
from jinja2 import Template
from config import *
import logging
import os

def get_template(template_name):
    try:
        template_file = open("%s/%s" % (TEMPLATE_DIR, template_name))
        template = Template(template_file.read())
        return template
    except IOError:
        raise jinja2.TemplateNotFound

def write_config(dest_file_path, ready_config):
    try:
        dest_file = open(dest_file_path, 'w')
        dest_file.write(ready_config)
        dest_file.close()
    except IOError, exc:
        logging.error("I/O Error. %s" % exc)
        raise
    logging.debug("Config written to file %s" % dest_file_path)


def new_vhost(config_template, params, httpd="nginx"):
    """
    Main Vhost-add procedure.
    """
    if httpd=="apache":
        available_dir = APACHE_CONFIG_DIR
    else:
        available_dir = NGINX_CONFIG_DIR

    config = get_template(config_template)
    ready_config = config.render(params)
    logging.debug("Template %s with parameters %s rendered." % (
        config_template,
        params
        )
    )
    logging.debug("Writing config into new file")
    dest_file_path = "%s/%s.conf" % (available_dir, params['domain'])
    write_config(dest_file_path, ready_config)


def enable_vhost(domain_name, httpd="nginx"):
    if httpd=="apache":
        enabled_dir = APACHE_ENABLED_DIR
        available_dir = APACHE_CONFIG_DIR
    else:
        enabled_dir = NGINX_ENABLED_DIR
        available_dir = NGINX_CONFIG_DIR

    logging.debug("Enabling vhost %s" % domain_name)
    enabled_path = "%s/%s.conf" % (enabled_dir, domain_name)
    available_path = "%s/%s.conf" % (available_dir, domain_name)
    os.symlink(available_path, enabled_path)
    logging.debug("Symlink done")

def disable_vhost(domain_name, delete=False, httpd="nginx"):
    if httpd=="apache":
        enabled_dir = APACHE_ENABLED_DIR
        available_dir = APACHE_CONFIG_DIR
    else:
        enabled_dir = NGINX_ENABLED_DIR
        available_dir = NGINX_CONFIG_DIR

    logging.debug("Disabling vhost %s on %s" % (domain_name, httpd))
    enabled_path = "%s/%s.conf" % (enabled_dir, domain_name)
    os.unlink(enabled_path)
    logging.debug("Symlink deleted")
    if delete:
        logging.debug("Deleting vhost %s on %s" % (domain_name, httpd))
        available_path = "%s/%s.conf" % (available_dir, domain_name)
        os.unlink(available_path)
        logging.debug("Config deleted")

def delete_vhost(domain_name, httpd="nginx"):
    disable_vhost(domain_name, delete=True, httpd=httpd)
