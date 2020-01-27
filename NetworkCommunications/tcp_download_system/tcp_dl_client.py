import ssl
import asyncio
import socket
import os
class QinClient:
	def __init__(self, host: str = '127.0.0.1', port: int = 18184):
		self._host = socket.gethostbyname(host)
		self._port = port
		self.crt = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tcp_download_system'))+'/ssl_cert/mycert.crt'

	async def send_message(self, message: str) -> dict:
		'''
		send_message() sends the given message to the server and
		returns the decoded callback response
		'''
		context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
		# 加载服务器所用证书和私钥
		context.load_verify_locations(self.crt)
		context.check_hostname = False
		reader, writer = await asyncio.open_connection(self._host, self._port, ssl=context)
		writer.write((message + '\r\n').encode())
		await writer.drain()
		raw = await reader.readuntil(b'\r\n')
		resp = raw.decode().strip()
		writer.close()
		await writer.wait_closed()
		return resp
if __name__ == "__main__":
	qc = QinClient()
	result = asyncio.run(qc.send_message('{"message":"https://www.youtube.com/watch?v=akCOiIzNszg&list=PLqgfngs2pxpQEQtx5JVNWjB00wWk4rZi6&index=2&t=0s","type":"youtube-dl","proxy":""}'))
	print(result)