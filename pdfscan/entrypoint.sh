#!/bin/bash
apt-get update
export DEBIAN_FRONTEND=noninteractive
apt-get install -y python3 python3-pip tesseract-ocr ffmpeg libsm6 libxext6
pip3 install pytesseract opencv-python
cd /home/pdfscan
python3 scan.py > pdfscanout.txt
tail -f /dev/null
