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

    if not os.path.exists('versions'):
        local('mkdir -p versions')
    else:
        pass

    arc_path = 'versions/webstatic{}.tgz'.format(datentime)
    stat = local('tar -cvzf {} web_static'.format(arc_path))
    if stat.succeeded:
        return arc_path
    else:
        return None
