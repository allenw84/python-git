#!/bin/bash

sudo apt-get update && sudo apt-get -y install python3.5

wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip3 install setuptools --upgrade
sudo apt-get install -y python3.5-venv
export LC_ALL="en_US.UTF-8"

python3 -m venv multicastenv
cd multicastenv
source bin/activate

git clone https://github.com/allenw84/vm_environment.git
tar zxvf vm_environment/multicast.tar.gz

cd multicast
sleep 5
python server.py
