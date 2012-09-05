#!/usr/bin/env python
#coding: utf-8

import config
import utils
import os

def new_vhost(config_template, params):
    utils.new_vhost(config_template, params, httpd="nginx")

def add_proxy_vhost(domain_name):
    """
    Proxy-vhost wrapper
    """
    new_vhost(
        config_template="nginx_proxy.conf",
        params={'domain': domain_name}
        )


def add_uwsgi_vhost(domain_name, document_root):
    """
    uWSGI Vhosts wrapper
    """
    new_vhost(
        config_template="nginx_uwsgi.conf",
        params={
            'domain': domain_name,
            'document_root': document_root
        }
    )


def enable_vhost(domain_name):
    utils.enable_vhost(domain_name, httpd="nginx")

def disable_vhost(domain_name):
    utils.disable_vhost(domain_name, httpd="nginx")

def delete_vhost(domain_name):
    utils.disable_vhost(domain_name, delete=True, httpd="nginx")

def vhost_exists(domain_name):
    exists = '%s.conf' % domain_name in os.listdir(config.NGINX_ENABLED_DIR)
    return exists
