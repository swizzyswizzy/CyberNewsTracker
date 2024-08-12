# Copy configuration files to nginx
cp nginx_configuration_files/* /etc/nginx

# Frontend of the website
# ...
# ...


# Copy frontend files to nginx directory
cp src/* /usr/share/nginx/html
cp -r static/ /usr/share/nginx/html

# Reloading nginx
systemctl reload nginx
