import sys, os
import socket
import threading
from time import ctime
#wget http://106.87.41.203:8000/DeployMagicWandAIServer.py
def DeployServer():
	
	os.chdir(os.getcwd())
	os.system("apt-get update && apt-get -y install python3 git screen && git clone https://qinbatista:qinyupeng1@bitbucket.org/qinbatista/magicwandaisample.git")
	os.system("apt-get install python3")
	os.system("apt-get -y install screen git iptraf")
	os.system("ssh-keygen")
	os.system("git clone https://qinbatista:qinyupeng1@bitbucket.org/qinbatista/magicwandaisample.git")
	os.system("python3 /root/magicwandaisample/10_搭建SSR服务器/10_搭建SSR服务器.py")
	# os.system("python3 /root/magicwandaisample/06_搭建代理IP服务器/06_搭建代理IP服务器.py")
	# os.system("git clone https://qinbatista:qinyupeng1@bitbucket.org/qinbatista/magicwandaiserver.git")
	# os.chdir("magicwandaiserver")
	# os.system("git submodule init")
	# os.system("git submodule update")
	# os.system("python3 DeployMagicWandAIWeb.py")

	os.system("python3 /root/magicwandaisample/03_动态DNS解析/01_Server.py")
def main():
	DeployServer()
if __name__ == '__main__':
    main()