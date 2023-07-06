#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import sudo, run, local
from datetime import datetime
import os

def do_pack():
    datentime = str(datetime.now()).split(sep='.')[0]
    datentime = datentime.replace(' ', '').replace(':', '').replace('-', '')
    if not os.path.exists('versions'):
        local('mkdir -p versions')

    arc_path = 'versions/webstatic{}.tgz'.format(datentime)
    stat = local('tar -cvzf {} web_static'.format(arc_path))
    if stat.succeeded:
        return arc_path
    else:
        return None

