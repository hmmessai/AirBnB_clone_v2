#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import sudo, run, local
from datetime import datetime


def do_pack():
    """Creates a tar file from web_static"""
    datentime = str(datetime.now()).split(sep='.')[0]
    datentime = datentime.replace(' ', '').replace(':', '').replace('-', '')
    local('tar -cvzf versions/web_static_{}.tar.gz web_static'.format(datentime))
