#!/usr/bin/python3
"""
This module contains the function do_pack that generates a .tgz archive
from the contents of the web_static folder (fabric script).

"""
from fabric.api import *
from datetime import datetime

def do_pack():
    """
    Fabric script that generates a .tgz archive from the contents of the
    web_static folder.
    """
    archive = 'web_static_' + date
    time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    result = local("sudo tar -cvzf versions/{} web_static".format(archive))
    if create is not None:
        return archive
    else:
        return None
