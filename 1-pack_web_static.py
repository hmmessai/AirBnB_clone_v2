"""
Generates a .tgz archive from the contents of the web_static folder
"""
from fabric.api import sudo, run, local
from 

def do_pack():
	local(tar -cvzf "versions/web_static{}{}{}{}{}{}.tgz".format
			() web_static)
