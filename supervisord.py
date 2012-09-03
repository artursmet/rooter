#!/usr/bin/env python
import config
import utils

def new_app(app_name, app_dir):
    app_template = utils.get_template("supervisor.conf")
    app_conf = app_template.render({
        'app_name': app_name,
        'app_dir': app_dir
        })
    dest_config = "%s/%s.conf" % (config.SUPERVISOR_DIR, app_name)
    utils.write_config(dest_config, app_conf)
