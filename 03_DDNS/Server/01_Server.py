import sys, os
import os.path
import socket
import threading
from socket import *
from time import ctime

YourDomainName = ""
host = '' #监听所有的ip
port = 12345 #接口必须一致
bufsize = 1024
addr = (host,port) 
udpServer = socket(AF_INET,SOCK_DGRAM)
udpServer.bind(addr) #开始监听

def ReplaceKeyWord(_Path,keyword,nextLine):
	print("_Path="+_Path)
	if os.path.isfile(_Path):
		file_object = open(_Path,encoding="utf8")
	JavaCode=[]
	try:
		all_the_text = file_object.readlines()
		for i in all_the_text:
			if(i.find(keyword)!=-1):
				JavaCode.append(nextLine+"\n")
			else:
				JavaCode.append(i)
	finally:
		file_object.close( )

	file_object_read = open(_Path,'w',encoding="utf8")
	try:
		file_object_read.writelines(JavaCode)
	finally:
		file_object_read.close()
def get_host_ip():
	try:
		s = socket(AF_INET, SOCK_DGRAM)
		s.connect(('8.8.8.8', 80))
		ip = s.getsockname()[0]
	finally:
		s.close()
	return ip
def DeployDNS():
	os.system("apt-get -y install dnsmasq")
	os.system("cp "+"./dnsmasq.conf /etc/dnsmasq.conf")
	ReplaceKeyWord("./dnsmasq.conf","listen-address=","listen-address="+get_host_ip()+",127.0.0.1")
	os.system("cp "+"./MyDNSHost /etc/hosts")
	os.system("/etc/init.d/dnsmasq restart")
def main():
	thread1 = threading.Thread(target=run,name="线程1",args=("123","123"))
	thread1.start()
	SyncDNSHost()
def SyncDNSHost():
	HostContext=[]
	global IPList,NumberList
	for index,i in enumerate(IPList):
		HostContext.append(i+" remote"+str(NumberList[index])+".magicwandai.com\n")
	file_object_read = open("./MyDNSHost",'w',encoding="utf8")
	try:
		file_object_read.writelines(HostContext)
	finally:
		file_object_read.close()
	threading.Timer(20,SyncDNSHost).start()
	os.system("cp "+"./MyDNSHost /etc/hosts")
	os.system("/etc/init.d/dnsmasq restart")
IPList=[]
MacList=[]
NumberList=[]
def run(param1,param2):
	DeployDNS()
	global IPList,MacList,NumberList
	DeployDNS()
	IPList = []
	MacList = []
	NumberList = []
	while True:
		data,addr = udpServer.recvfrom(bufsize) 
		ReciveIP, _ = addr
		data  = data.decode(encoding='utf-8').upper()
		print("Recive:"+ReciveIP+"->["+data+"]")
		my = data.split("|")
		#没有相同ip没有相同mac说明是新机器需要记录
		if IPList.count(ReciveIP)==0 and MacList.count(my[0])==0:
			IPList.append(ReciveIP)
			MacList.append(my[0])
			NumberList.append(my[1])
		#有相同ip却有不同mac说明同一网段重复提交，更新mac
		elif IPList.count(ReciveIP)!=0 and MacList.count(my[0])==0:
			MacList[IPList.index(ReciveIP)]= my[0]
		#没有相同ip有相同mac说明ip地址被改变需要重写记录
		elif IPList.count(ReciveIP)==0 and MacList.count(my[0])!=0:
			IPList[MacList.index(my[0])]= ReciveIP
		#有相同ip却有相同mac说明重复提交，保持不变
		else:
			NumberList[IPList.index(ReciveIP)]= my[1]
	udpServer.close()

if __name__ == '__main__':
	main()