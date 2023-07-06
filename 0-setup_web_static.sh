#!/usr/bin/env bash
# Sets up  web server to deploy web static

# Install Nginx 
sudo apt-get install nginx

# Make sure the folder /data/web_static/releases exist
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake html file to test
sudo touch /data/web_static/releases/test/index.html
echo 'Testing!' | tee /data/web_static/releases/test/index.html

# Create symbolic link
ln -s -f -T /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to server web_static
replacement="server_name _;\n\n\tlocation ^~ \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}"
if (grep hbnb_static /etc/nginx/sites-available/default)
then
        :
else
        sudo sed -i "s/server_name _;/$replacement/" /etc/nginx/sites-available/default
fi
sudo service nginx restart
