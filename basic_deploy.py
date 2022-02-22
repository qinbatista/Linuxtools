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
	# os.system("bash ./DebugTool/12_install_python3/install_python-x.sh")
	# os.system("python ./DebugTool/02_pip3/get-pip.py")
	os.system("curl -fsSL https://test.docker.com -o test-docker.sh")
	os.system("sh test-docker.sh")
	os.system("apt-get install docker-ce docker-ce-cli containerd.io")
	os.system("wget https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py")
	os.system("docker run -itdv /root/download:/download -p 10005:10005  qinbatista/download")
	os.system("cp ./speedtest.py /usr/local/bin/")
	os.system("docker run -itd -p 7000-7030:7000-7030  qinbatista/ssr")
	os.system("iptables -A INPUT -p udp --dport 12345 -j ACCEPT")
	os.system("iptables -A INPUT -p udp --dport 53 -j ACCEPT")
	os.system("iptables-save")
	

if __name__ == '__main__':
	DeployServer()