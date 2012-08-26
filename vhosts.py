import nginx
import apache
import utils
import logging

def add_vhost(domain_name, document_root, vhost_type):
    if vhost_type == 'php':
        nginx.add_proxy_vhost(domain_name)
        nginx.enable_vhost(domain_name)
        apache.add_php_vhost(domain_name, document_root)
        apache.enable_vhost(domain_name)
    elif vhost_type == 'uwsgi':
        nginx.add_uwsgi_vhost(domain_name, document_root)
        nginx.enable_vhost(domain_name)

def delete_vhost(domain_name):
    logging.debug("Deleting vhost %s" % domain_name)
    try:
        utils.delete_vhost(domain_name, httpd="nginx")
        utils.delete_vhost(domain_name, httpd="apache")
    except Exception, exc:
        logging.error("Something went wrong: %s" % exc)

