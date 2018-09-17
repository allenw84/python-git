#!/bin/bash
mkdir mnetlab731testfolder
sudo apt-get update && sudo apt-get install -y iperf screen default-jre
screen -d -m -S client wget -O hello.jar http://mnet.cs.nthu.edu.tw/mnet_old/Chang/hello.jar
screen -d -m -S client wget -O Setting http://mnet.cs.nthu.edu.tw/mnet_old/Chang/Setting
sleep 5
screen -d -m -S client java -jar hello.jar
