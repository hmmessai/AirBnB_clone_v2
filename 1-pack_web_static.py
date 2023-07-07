#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import sudo, run, local
from datetime import datetime
import os


def do_pack():
    """Creates an archive file from files inside web_static"""
    datentime = str(datetime.now()).split(sep='.')[0]
    datentime = datentime.replace(' ', '').replace(':', '').replace('-', '')

    if not os.path.isdir('versions'):
        if local('mkdir -p versions').failed is True:
            return None
    arc_path = 'versions/web_static_{}.tgz'.format(datentime)
    if local('tar -zcvf {} web_static'.format(arc_path)).failed is True:
        return None
    return arc_path
