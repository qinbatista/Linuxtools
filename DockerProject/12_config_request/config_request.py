import os
import sys
import time
import json
import random
import aiomysql
from aiohttp import web
import threading
class GameManager:
	def __init__(self, worlds = []):
		self.__iap_list_file = "iap_list.json"
		self.__updateverify_file = "updateverify.json"
		self.__store_file = "store.json"
		self.__game_list = '/Users/batista/SingmaanProject/OperationLives'#'/Users/batista/SingmaanProject/OperationLives'#'/root/OperationLives'
		self.__game_names = []
		self.__all_iap_config = {}
		self.__all_updateverify_config = {}
		self.__all_store_config = {}
		self._set_all_config()

	def _message_typesetting(self, status: int, message: str, data: dict = {}) -> dict:
		return {"status": status, "message": message, "data": data}

	def _set_all_config(self):
		thread1 = threading.Thread(target=self._config_update)
		thread1.start()

	def _config_update(self):
		while True:
			print("start reading config")
			self.__all_iap_config = {}
			self.__all_updateverify_config = {}
			folder_list = os.listdir(self.__game_list)
			for game_name in folder_list:
				if game_name.rfind("")!=-1 and game_name.rfind(".")!=-1:
					continue
				#add iap_list.json
				if os.path.exists(f"{self.__game_list}/{game_name}/{self.__iap_list_file}"):
					with open(f"{self.__game_list}/{game_name}/{self.__iap_list_file}", 'r') as f:
						self.__all_iap_config[game_name] = json.load(f)

				#add updateverify.json
				if os.path.exists(f"{self.__game_list}/{game_name}/{self.__updateverify_file}"):
					with open(f"{self.__game_list}/{game_name}/{self.__updateverify_file}", 'r') as f:
						self.__all_updateverify_config[game_name] = json.load(f)

				#add store.json
				if os.path.exists(f"{self.__game_list}/{game_name}/{self.__store_file}"):
					with open(f"{self.__game_list}/{game_name}/{self.__store_file}", 'r') as f:
						print(game_name+":store")
						self.__all_store_config[game_name] = json.load(f)
			print("end reading config")
			time.sleep(60*60*24)
			print("restart reading config")

	async def get_iap(self, game_name:str):
		if game_name not in self.__all_iap_config:
			return self._message_typesetting(400,"error",{"status":"200","message":"don't have such game config:"+game_name})
		else:
			return self._message_typesetting(200,"got config success",{"result":self.__all_iap_config[game_name]})

	async def get_update_verify(self, game_name:str):
		if game_name not in self.__all_updateverify_config:
			return self._message_typesetting(400,"error",{"status":"200","message":"don't have such game config:"+game_name})
		else:
			return self._message_typesetting(200,"got config success",{"result":self.__all_updateverify_config[game_name]})

	async def store(self, game_name:str):
		if game_name not in self.__all_store_config:
			return self._message_typesetting(400,"error",{"status":"200","message":"don't have such game config:"+game_name})
		else:
			return self._message_typesetting(200,"got config success",{"result":self.__all_store_config[game_name]})

ROUTES = web.RouteTableDef()
def _json_response(body: dict = "", **kwargs) -> web.Response:
	kwargs['body'] = json.dumps(body or kwargs['kwargs']).encode('utf-8')
	kwargs['content_type'] = 'text/json'
	return web.Response(**kwargs)

#json param, get result from request post
#http://localhost:10001/get_iap?gamename=ww1
@ROUTES.post('/get_iap')
async def _get_iap(request: web.Request) -> web.Response:
	query = request.query
	result = await (request.app['MANAGER']).get_iap(query['gamename'])
	return _json_response(result)

#json param, get OperationLives
#http://localhost:10001/get_update_verify?game_name=ww1
@ROUTES.post('/get_update_verify')
async def _get_update_verify(request: web.Request) -> web.Response:
	query = request.query
	result = await (request.app['MANAGER']).get_update_verify(query['gamename'])
	return _json_response(result)

#json param, get OperationLives
#http://office.singmaan.com:10001/store?game_name=TerraGenesis
@ROUTES.post('/store')
async def _store(request: web.Request) -> web.Response:
	query = request.query
	result = await (request.app['MANAGER']).store(query['gamename'])
	return _json_response(result)


def run():
	print("version:1.0")
	app = web.Application()
	app.add_routes(ROUTES)
	app['MANAGER'] = GameManager()
	web.run_app(app, port = "10001")


if __name__ == '__main__':
	run()
