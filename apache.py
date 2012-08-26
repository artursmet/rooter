#!/usr/bin/env python
#coding: utf-8

from config import *
from utils import get_template

def add_php_vhost(domain_name, document_root):
    config = get_template("apache_php.conf")
    ready_config = config.render(
                        domain=domain_name,
                        document_root=document_root
                    )
    dest_file_path = "%s/%s.conf" % (APACHE_CONFIG_DIR, domain_name)

    try:
        dest_file = open(dest_file_path, 'w')
        dest_file.write(ready_config)
        dest_file.close()
    except IOError, exc:
        logging.error("I/O Error %s" %s)
        raise

    logging.debug("Config written to file %s" % dest_file_path)

def enable_vhost(domain_name):
    enabled_path = "%s/%s.conf" % (APACHE_ENABLED_DIR, domain_name)
    available_path = "%s/%s.conf" % (APACHE_CONFIG_DIR, domain_name)
    subprocess.call("ln -s %s %s" % (enabled_path, available_path))
