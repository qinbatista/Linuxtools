#coding=UTF-8
import asyncio
import sys
import ssl
import json
import os
class QinServer:
	def __init__(self, host: str = '127.0.0.1', port: int = 10000):
		self._host = host
		self._port = port
		self._crt = '/Users/batista/MyProject/lukseunserversys/gate/cert/mycert.crt'
		self._key = '/Users/batista/MyProject/lukseunserversys/gate/cert/rsa_private.key'
		self._password = 'lukseun1'

	async def __echo(self,reader, writer):
		address = writer.get_extra_info('peername')
		data = await reader.readuntil(b'\r\n')
		resp = data.decode().strip()
		message,msg_type =self.parse_message(resp)
		writer.write(b'get your message:'+(self.__mission_manager(message,msg_type)).encode('utf-8')+"->".encode('utf-8')+message.encode('utf-8')+b'\r\n')
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

	def parse_message(self,msg):
		my_json = json.loads(msg)
		return my_json["message"],my_json["type"]

	def __mission_manager(self,message,type):
		if type == "youtube_dl":
			os.system('proxychains youtube_dl '+message)
			return "[youtube_dl] downloading:"+message
		elif type == "wget":
			os.system('proxychains wget '+message)
			return "[wget] downloading:"+message
		elif type =="instagram-scraper":
			os.system('proxychains instagram-scraper '+message)
			return "[instagram-scraper] downloading:"+message

if __name__ == "__main__":
	qs = QinServer()
	qs.start_server()