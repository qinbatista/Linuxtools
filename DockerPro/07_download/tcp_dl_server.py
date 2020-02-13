#coding=UTF-8
import asyncio
import sys
import ssl
import json
import os
from datetime import datetime
import threading
class QinServer:
	def __init__(self, host: str = '', port: int = 18184):
		self._host = host
		self._port = port
		self._crt = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tcp_download_system'))+'/ssl_cert/mycert.crt'
		self._key = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tcp_download_system'))+'/ssl_cert/rsa_private.key'
		self._password = 'lukseun1'
		self._exclude_files=['ssl_cert','tcp_dl_client.py','tcp_dl_server.py','.DS_Store']
		self._root_folder = '/Users/batista/Desktop/download'#'/root/download' #'/Users/batista/Desktop/download'
		self._cache_folder = '/Users/batista/Desktop/deliveried'#'/root/deliveried' #'/Users/batista/Desktop/deliveried'

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
		print("111")
		os.system(command)
		print("222")
		while os.path.exists(file_name):
			print('1')
		file_name_lists = os.listdir('.')
		# print(file_name_lists)
		for file_name in file_name_lists:
		# 	print(1)
			if file_name not in self._exclude_files:
				os.system(f'mv {file_name} /{self._root_folder}/{file_name}')
		# 		#sync files
		# 		print(4)
		# 		os.system(f'rsync -avz --progress -e "ssh -p 10022" /{self._root_folder} root@cqhome.qinbatista.com:{self._root_folder}/')
		# 		os.system(f'mv {self._root_folder}/{file_name}/ /{self._root_folder}')

	def __thread_download(self,command):
		thread1 = threading.Thread(target=self.__command, name="t1",args=(command,''))
		thread1.start()

	async def __mission_manager(self,message,type,proxy):
		if proxy!='': proxy = 'proxychains'
		if   type == "youtube-dl": self.__thread_download(f'{proxy} {type} {message}')
		elif type == "wget": self.__thread_download(f'{proxy} {type} {message}')
		elif type == "instagram-scraper": self.__thread_download(f'{proxy} {type} {message}')


if __name__ == "__main__":
	qs = QinServer()
	qs.start_server()

