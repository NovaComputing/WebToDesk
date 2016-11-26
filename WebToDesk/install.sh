#!/bin/bash

sudo apt-get install python-pip
pip install selenium

sudo mkdir /opt/WebToDesk/
sudo mkdir /opt/WebToDesk/bin/
sudo mkdir /opt/WebToDesk/bashAssets/

sudo chmod o+r+w /opt/WebViewer/*
sudo cp ~/Downloads/WebToDesk/Python /opt/WebToDesk/bin/
sudo cp ~/Downloads/WebToDesk/etc/WebViewer.txt /etc/WebToDesk.txt
sudo cp ~/Downloads/WebToDesk/scripts/* /opt/WebToDesk/bin/
sudo cp ~/Downloads/WebToDesk/Assets/* /opt/WebToDesk/assets/
sudo cp ~/Downloads/WebToDesk/iconFiles/* ~/Desktop/
