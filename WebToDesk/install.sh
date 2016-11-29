#!/bin/bash

sudo apt-get install python-pip
pip install selenium

sudo mkdir /opt/WebToDesk/
sudo mkdir /opt/WebToDesk/bin/
sudo mkdir /opt/WebToDesk/assets/

sudo chmod o+r+w /opt/WebViewer/*
sudo cp ~/Downloads/WebToDesk/Python/WebToDesk.py /opt/WebToDesk/bin/
sudo cp ~/Downloads/WebToDesk/etc/WebViewer.txt /etc/
sudo cp ~/Downloads/WebToDesk/scripts/* /usr/bin/
sudo cp ~/Downloads/WebToDesk/Assets/* /opt/WebToDesk/assets/
sudo cp ~/Downloads/WebToDesk/iconFiles/* ~/Desktop/
