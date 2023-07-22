#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import sudo, run, local, put, env
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['web-02.hmmessai.tech', 'web-01.hmmessai.tech']


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


def do_deploy(archive_path):
    """
    Deploying archive to a remote server
    Arguments:
        archive_path(str): the path to the archive to
            be deployed on the server
    """
    if not os.path.isfile(archive_path):
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed:
        return False

    if run("mkdir -p /data/web_static/releases/{}".format(name)).failed:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(file, name)).failed:
        return False
    if run("rm /tmp/{}".format(file)).failed:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}".format(name, name)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed:
        return False
    return True

def deploy():
    """
    Creates and archive and deploy it to servers
    """
    path = do_pack()
    if path is None:
        return False
    exit_status = do_deploy(path)
    return exit_status

def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    if number == 1 or number == 0:
        path = do_pack()
        folder = path.split("/")[-1].split(".")[0]
        
    elif number == 2:
        path = do_pack()
