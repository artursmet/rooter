rooter
======

Set of python scripts for creating vhosts on servers.

Basic usage
===========

./rooter.py --add --type php /home/someuser/public_html --domain myuser.mydomain.tld

Above command creates nginx reverse proxy vhost and Apache php vhost.

uWSGI apps
==========

Rooter can automaticaly detect uWSGI apps in defined directory (/srv/django/ by default)

* Create virtualenv for app in /srv/django/myapp.domain.tld
* Install requirements for app
* Create uwsgi.ini for this app and save in /srv/django/myapp.domain.tld/uwsgi.ini
* Run detect_uwsgi.py
* Rooter will create: 
>* nginx vhost for uWSGI application
>* supervisord configuration for uwsgi process

TODO:
* autostart for new supervisord-controlled apps
* fully automatic deployment for new applications (user should  provide only git repo URI and domain)

