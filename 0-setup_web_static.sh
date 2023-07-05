#!/usr/bin/env bash
# Sets up  web server to deploy web static

# Install Nginx 
sudo apt-get install nginx

# Make sure the folder /data/web_static/releases exist
mkdir -p /data/web_staic/releases/test/

# Make sure the folder /data/web_static/shared exists
mkdir -p /data/web_static/shared/

# Create a fake html file to test
touch /data/web_static/releases/test/index.html
echo 'Testing!' > /data/web_static/releases/test/index.html

# Create symbolic link
ln -s -d /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to server web_static
replacement="server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}"
sed -i "s/server_name _;/$replacement/" /etc/nginx/sites-available/default
