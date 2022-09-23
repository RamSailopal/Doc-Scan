#!/bin/bash
apt-get update
export DEBIAN_FRONTEND=noninteractive
apt-get install -y apache2
sleep 60 
cp /home/webserver/qrcode* /var/www/html/
cp /home/webserver/sample.js /var/www/html/
cp /home/webserver/style.css /var/www/html/
cp /home/pdfconvert/page0.jpg /var/www/html/
cp /var/www/html/qrcode.html /var/www/html/index.html
service apache2 start
tail -f /dev/null
