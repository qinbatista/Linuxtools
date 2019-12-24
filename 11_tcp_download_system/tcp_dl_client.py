import ssl
import asyncio
class QinClient:
	def __init__(self, host: str = '127.0.0.1', port: int = 10000):
		self._host = host
		self._port = port
		self.crt = '/Users/batista/MyProject/lukseunserversys/gate/cert/mycert.crt'

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
	result = asyncio.run(qc.send_message('{"message":"aaaa","type":"youtube_dl"}'))
	print(result)