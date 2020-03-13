#coding=UTF-8
import asyncio
import sys
import ssl
import json
import os
from datetime import datetime
import threading
import subprocess
import time
from subprocess import Popen, PIPE
class QinServer:
	def __init__(self, host: str = '', port: int = 18184):
		self._host = host
		self._port = port
		self._crt = '/mycert.crt'
		self._key = '/rsa_private.key'
		self._password = 'lukseun1'
		self._exclude_files=['ssl_cert','tcp_dl_client.py','tcp_dl_server.py','.DS_Store']
		self._root_folder = '/root/download'
		self._cache_folder = '/root/deliveried'
		# if not os.path.exists(self._root_folder):os.makedirs(self._root_folder)
		# if not os.path.exists(self._cache_folder):os.makedirs(self._cache_folder)

	async def __echo(self,reader, writer):
		address = writer.get_extra_info('peername')
		data = await reader.readuntil(b'\r\n')
		resp = data.decode().strip()
		message,msg_type,proxy =self.__parse_message(resp)
		await self.__mission_manager(message,msg_type,proxy)
		writer.write(b'start downloading'+"->".encode('utf-8')+message.encode('utf-8')+b'\r\n')
		await writer.drain()

	def start_server(self):
		SERVER_ADDRESS = (self._host, self._port)
		event_loop = asyncio.get_event_loop()
		ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
		ssl_context.check_hostname = False
		ssl_context.load_cert_chain(self._crt, self._key,password = self._password)
		factory = asyncio.start_server(self.__echo, *SERVER_ADDRESS, ssl=ssl_context)
		server = event_loop.run_until_complete(factory)
		print('starting up on {} port {}'.format(*SERVER_ADDRESS))
		try:
			event_loop.run_forever()
		except KeyboardInterrupt:
			pass
		finally:
			server.close()
			event_loop.run_until_complete(server.wait_closed())
			print('closing event loop')
			event_loop.close()

	def __parse_message(self,msg):
		my_json = json.loads(msg)
		return my_json["message"],my_json["type"],my_json["proxy"]

	def __command(self,command,args):
		#download files
		current_milli_time = lambda: int(round(time.time() * 1000))
		task_id = str(current_milli_time())
		os.mkdir(f'{self._root_folder}/{task_id}')
		os.chdir(f'{self._root_folder}/{task_id}')
		print("command:"+command)
		p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
		p.wait()
		print(str(os.listdir('.')))
		# print(f'rsync -avz --progress -e "ssh -p 10022" {self._root_folder}/{task_id} root@cqhome.qinbatista.com:{self._root_folder}/')
		p = subprocess.Popen(f'rsync -avz --progress -e "ssh -p 10022" {self._root_folder}/{task_id} root@cqhome.qinbatista.com:{self._root_folder}/', stdout=subprocess.PIPE, shell=True)
		p.wait()
		os.system('ls')
		os.system('pwd')
		for file in os.listdir('.'):
			print(f"mv {self._root_folder}/{task_id}/* {self._cache_folder}......")
			os.system(f"mv {self._root_folder}/{task_id}/* {self._cache_folder}")


	def __thread_download(self,command):
		thread1 = threading.Thread(target=self.__command, name="t1",args=(command,''))
		thread1.start()

	async def __mission_manager(self,message,type,proxy):
		if proxy!='': proxy = 'proxychains'
		if   type == "youtube-dl": self.__thread_download(f'{proxy} {type} {message}')
		elif type == "wget": self.__thread_download(f'{proxy} {type} {message}')
		elif type == "instagram-scraper": self.__thread_download(f'{proxy} {type} {message}')
		elif type == "aria2c": self.__thread_download(f'{proxy} {type} {message}')

if __name__ == "__main__":
	current_milli_time = lambda: int(round(time.time() * 1000))
	task_id = current_milli_time()
	os.system("cat  ~/.ssh/id_rsa.pub")
	os.system('rsync -avz --progress -e "ssh -o stricthostkeychecking=no -p 10022" ~/download root@cqhome.qinbatista.com:~/')
	qs = QinServer()
	qs.start_server()


	# p = subprocess.Popen('youtube-dl https://www.youtube.com/watch?v=20LTayRXtAg', stdout=subprocess.PIPE, shell=True)
	# # (output, err) = p.communicate()
	# #This makes the wait possible
	# p.wait()
	# print("p_status="+str(p_status))

