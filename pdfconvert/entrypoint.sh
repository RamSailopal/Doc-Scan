#!/bin/bash
apt-get update
apt-get install -y wget python3 python3-pip poppler-utils
pip3 install pdf2image
cd /home/pdfconvert
wget https://www.va.gov/vaforms/va/pdf/VA0730b.pdf
python3 convert.py
