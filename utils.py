#!/usr/bin/env python
from jinja2 import Template
from config import TEMPLATE_DIR

def get_template(template_name):
    try:
        template_file = open("%s/%s" % (TEMPLATE_DIR, template_name))
        template = Template(template_file.read())
        return template
    except IOError:
        raise jinja2.TemplateNotFound


