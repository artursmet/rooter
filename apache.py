#!/usr/bin/env python
#coding: utf-8

from config import *
import utils

def add_php_vhost(domain_name, document_root):
    utils.new_vhost(config_template="apache_php.conf",
        params={
            'domain': domain_name,
            'document_root': document_root
        },
        httpd="apache"
    )

def enable_vhost(domain_name):
    utils.enable_vhost(domain_name, httpd="apache")

def disable_vhost(domain_name):
    utils.disable_vhost(domain_name, httpd="apache")

def delete_vhost(domain_name):
    utils.disable_vhost(domain_name, delete=True, httpd="apache")

