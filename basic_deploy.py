import sys, os
import socket
import threading
from time import ctime

def DeployServer():
	
	os.chdir(os.getcwd())
	#open root
	#install basic tool
	os.system("apt-get update && apt-get -y install python3 git screen iptraf")
	#open bbr
	os.system('echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf')
	os.system('echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf')
	os.system('sysctl -p')
	os.system('sysctl net.ipv4.tcp_available_congestion_control')
	#check if bbr is opening: lsmod | grep bbr

	os.system("cp ./DebugTool/11_iptest/iptest.py /usr/local/bin/")
	os.system("bash ./DebugTool/12_install_python3/install_python-x.sh")
	os.system("python ./DebugTool/02_pip3/get-pip.py")
	os.system("curl -fsSL https://get.docker.com -o get-docker.sh")
	os.system("sh get-docker.sh")
	os.system("wget https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py")
	os.system("cp ./speedtest.py /usr/local/bin/")
	os.system("docker run -itd -p 7000-7030:7000-7030  qinbatista/ssr")
	os.system("docker run -itdv /root/download:/root/download -v /root/deliveried:/root/deliveried -p 10022:22 -p 18184:18184  qinbatista/download")

if __name__ == '__main__':
	DeployServer()