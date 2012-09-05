#!/usr/bin/env python
#coding: utf-8
import os
import nginx
import supervisord
import socket
import logging

def detect_apps(srv_dir, dry_run=False):
    dirs = os.listdir(srv_dir)
    os.chdir(srv_dir)
    for d in dirs:
        # Check if domain is active (DNS check)
        try:
            ip = socket.gethostbyname(d)
        except socket.gaierror:
            logging.warning("Wrong directory name: %s." % d)
            continue

        if "uwsgi.ini" in os.listdir(d):
            # We've found uWSGI app!
            # Now create nginx vhost based on dir name
            if dry_run:
                logging.info("uWSGI app found in %s" % d)
            else:
                nginx.add_uwsgi_vhost(
                        domain_name=d,
                        document_root=d
                        )
                # Enable supervisord for uWSGI process
                supervisord.new_app(app_name=d, app_dir=d)
                nginx.enable_vhost(d)


