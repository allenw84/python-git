#!/bin/bash

#unicast python3
#sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update && sudo apt-get -y install python3.5  (already installed)

wget https://bootstrap.pypa.io/get-pip.py  #install pip
sudo python3 get-pip.py 
sudo pip3 install setuptools --upgrade

sudo apt-get -y install python3.5-venv #build virtulenv
export LC_ALL="en_US.UTF-8"  #set environment variable

python3 -m venv unicastenv
cd unicastenv
source bin/activate

git clone https://github.com/allenw84/python-git.git #download and unzip
tar zxvf python-git.git/unicast2.tar.gz

cd unicast
pip3 install -r requirements.txt #install the kit
sleep 5
python app.py
