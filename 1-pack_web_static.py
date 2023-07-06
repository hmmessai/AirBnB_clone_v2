#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import sudo, run, local
from datetime import datetime
import os

def do_pack():
    """Creates a tar file from web_static"""
    datentime = str(datetime.now()).split(sep='.')[0]
    datentime = datentime.replace(' ', '').replace(':', '').replace('-', '')
    local('tar -cvzf arc_path web_static'.format(datentime))
