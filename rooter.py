#!/usr/bin/env python
#coding: utf-8

import optparse
from config import *
import vhosts

parser = optparse.OptionParser()

parser.add_option('-a', '--add',
    help="Add Vhost",
    dest="add",
    action="store_true",
    )

parser.add_option('-d', '--delete', help="Remove Vhost",
    action="store_true",
    dest="delete"
    )

parser.add_option('-t', '--type',
                      type='choice',
                      action='store',
                      dest='vhost_type',
                      choices=['php', 'uwsgi'],
                      default='php',
                      help='Vhost type. Choices: php / uwsgi',)

parser.add_option('--domain',
    help="Domain Name",
    type="string",
    dest="domain_name"
    )
parser.add_option('--root',
    help="Document Root",
    type="string",
    dest="docroot"
    )

(opts, args) = parser.parse_args()

if opts.add and opts.delete:
    print "Use only one mode --add OR --delete\n"
    parser.print_help()
    exit(-1)

if opts.delete:
    if not opts.domain_name:
        print "Bad usage. No domain name given."
        parser.print_help()
        exit(-1)
    else:
        vhosts.delete_vhost(opts.domain_name)

if opts.add:
    if opts.domain_name and opts.docroot and opts.vhost_type:
        vhosts.add_vhost(
            domain_name=opts.domain_name,
            document_root=opts.docroot,
            vhost_type=opts.vhost_type
        )
    else:
        print "Bad usage. Domain name, Document Root and Vhost type required"
        parser.print_help()
        exit(-1)
