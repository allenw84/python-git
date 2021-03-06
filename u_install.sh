#!/bin/bash
sudo apt-get update && sudo apt-get -y install python3.5
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip3 install setuptools --upgrade
sudo apt-get -y install python3.5-venv
export LC_ALL="en_US.UTF-8"
python3 -m venv unicastenv
cd unicastenv
source bin/activate
git clone https://github.com/allenw84/python-git.git
tar zxvf python-git/unicast.tar.gz
cd unicast
pip3 install -r requirements.txt
sleep 5 
python app.py

