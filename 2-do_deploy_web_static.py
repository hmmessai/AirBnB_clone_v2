#!/usr/bin/python3
"""Script that distributes an archive to the web_servers"""
import os
from fabric.api import env, put, run

env.user = 'ubuntu'
env.hosts = ['web-01.hmmessai.tech', 'web-02.hmmessai.tech']


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

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed is True:
        return False
    return True
