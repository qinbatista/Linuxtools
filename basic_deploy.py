import sys, os
import socket
import threading
from time import ctime

def DeployServer():
	os.chdir(os.getcwd())
	os.system("cp ./DebugTool/04_speedtest/speedtest.py /usr/local/bin/")
	os.system("cp ./DebugTool/11_iptest/iptest.py /usr/local/bin/")
	os.system("bash ./DebugTool/12_install_python3/install_python-x.sh")


if __name__ == '__main__':
	DeployServer()