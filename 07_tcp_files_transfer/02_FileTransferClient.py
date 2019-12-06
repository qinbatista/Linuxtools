#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 发送格式为 1字节的"文件名长度"+"文件名"+"二进制数据" 
# 如果文件名是 quit 那就退出

import os
from socket import socket, AF_INET, SOCK_STREAM
import hashlib
import threading
import time
from os.path import join, getsize
class SimpleClient:
	def __init__(self, *args, **kwargs):
		self.__sem = threading.Semaphore(value=5)#初始化信号量，最大并发数
		self.filesize=0
		return
	def setHost(self, host, port):
		self.host = host
		self.port = port
		self.s = socket(AF_INET, SOCK_STREAM)
		target = (self.host,self.port)
		self.s.connect(target)
	def __get_header (self,filepath):
			filename = self.SerializeFileName(filepath)#文件名
			md5 = self.getBigFileMD5(filepath)#md5
			self.filesize = self.SerializeFileSize(getsize(filepath))#文件大小
			msg = str(len(filename)) + filename + str(len(md5)) + md5 + str(len(self.filesize)) + self.filesize
			return msg
	def send(self,filepath):
			#生成文件头
			header = self.__get_header(filepath)
			self.s.send((header).encode()) #先发送头部
			header = self.s.recv(6).decode("utf-8")
			while header != "HEADER":
				print("[Client Msg] Connecting Failed")
				return False
			with open(filepath, 'rb') as f: #读取数据发送
				size = int(self.filesize.replace("π",""))
				while size!=0:
					if size>1024:
						buf = f.read(1024)
					else:
						buf = f.read(size)
					self.s.send(buf)
					if size>1024:
						size = size-1024
					else:
						size = 0
			msg = self.s.recv(4).decode("utf-8")
			if msg=="DONE":
				print("[Client Msg] Sent Success:"+filepath)
				self.s.close()
				return True
			else:
				print("[Client Msg] Send Failed:"+filepath)
				self.s.close()
				return False
			
	def SerializeHeader(self, msg):#整个头文件长度2位表示，文件大小1-99
		if len(msg)>99:
			print("[Client Message]	header over 99 bit")
			return ""
		if len(msg)<10:
			return "π"*(10-len(msg))+msg
	def SerializeFileName(self,filepath):#固定2个字节显示长度 名字长度范围1-99
		filename = os.path.basename(filepath)
		if len(filename)>99:
			print("[Client Message]	File Name is too long]")
			return ""
		if len(filename)<10:
			return "π"*(10-len(filename))+filename
		else:
			return filename
	def getBigFileMD5(self,filepath):#获取md5密码，长度32为，2个字节显示长度
		if os.path.isfile(filepath):
			md5obj = hashlib.md5()
			maxbuf = 8192
			f = open(filepath,'rb')
			while True:
				buf = f.read(maxbuf)
				if not buf:
					break
				md5obj.update(buf)
			f.close()
			hash = md5obj.hexdigest()
			return str(hash).upper()
	def SerializeFileSize(self, filesize):#固定1个字节显示长度，文件大小9位byte
		if len(str(filesize))<10:
			return str(int(str(filesize)))
		else:
			print("[Client Message]	File size can't over 1GB")
			return ""
if __name__ == '__main__':
	c = SimpleClient()
	c.setHost("155.138.198.201", 1234)
	c.send("/Users/yupengqin/Desktop/Unitykey.key") # 发送文件