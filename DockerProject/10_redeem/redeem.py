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
		self.__reedem_codes_file = 'redeem'
		self.__root_OperationLives = "/root/redeemsystem"#'/Users/batista/Desktop'#'/root/redeemsystem'
		self.__game_list = "/root/OperationLives"#'/Users/batista/SingmaanProject/OperationLives'#'/root/OperationLives'
		self.__game_names = []
		self.__max_redeems = 1000#40000
		self.__item_quantity = 50
		self.__redeem_codes = dict()
		self.__redeem_codes_list = []
		self.__all_redeem_codes = {}
		self.__count = 0
		self.__reedem_code_version = 0
		self._set_all_config()
	async def _connect_sql(self):
		self._pool = await aiomysql.create_pool(
				maxsize = 20,
				host = '192.168.1.102',
				user = 'root',
				password = 'lukseun',
				charset = 'utf8',
				autocommit = True)
	async def _execute_statement(self, database_name: int, statement: str) -> tuple:
		"""
		Executes the given statement and returns the result.
		执行给定的语句并返回结果。
		:param statement: Mysql执行的语句
		:return: 返回执行后的二维元组表
		使用例子：data = await self._execute_statement(world, 'SELECT ' + material + ' FROM player WHERE unique_id="' + str(unique_id) + '";')
		"""
		if self._pool is None: await self._connect_sql()
		async with self._pool.acquire() as conn:
			await conn.select_db(database_name)
			async with conn.cursor() as cursor:
				await cursor.execute(statement)
				return await cursor.fetchall()
	async def _execute_statement_update(self, database_name: int, statement: str) -> int:
		"""
		Execute the update or set statement and return the result.
		执行update或set语句并返回结果。
		:param statement: Mysql执行的语句
		:return: 返回update或者是set执行的结果
		使用例子：return await self._execute_statement_update(world, f"UPDATE player SET {material}={value} where unique_id='{unique_id}'")
		"""
		if self._pool is None: await self._connect_sql()
		async with self._pool.acquire() as conn:
			await conn.select_db(database_name)
			async with conn.cursor() as cursor:
				return await cursor.execute(statement)
	def _message_typesetting(self, status: int, message: str, data: dict = {}) -> dict:
		return {"status": status, "message": message, "data": data}

	def generate_verification_code(self):
		''' 随机生成6位的验证码 '''
		code_list = []
		for i in range(10): # 0-9数字
			code_list.append(str(i))
		for i in range(65, 91): # A-Z
			code_list.append(chr(i))
		for i in range(97, 123): # a-z
			code_list.append(chr(i))
		myslice = random.sample(code_list, 6)  # 从list中随机获取6个元素，作为一个片断返回
		verification_code = ''.join(myslice) # list to string
		return verification_code

	def _set_all_config(self):
		thread1 = threading.Thread(target=self._config_update)
		thread1.start()

	def _config_update(self):
		while True:
			self.__reedem_code_version = self.__reedem_code_version+1
			self.__game_names = []
			self.__redeem_codes = dict()
			self.__redeem_codes_list = []
			self.__all_redeem_codes = {}
			folder_list = os.listdir(self.__game_list)
			for game_name in folder_list:
				if game_name.rfind("")!=-1 and game_name.rfind(".")!=-1:
					continue
				print(game_name)
				self.__game_names.append(game_name)
				for i in range(0,self.__max_redeems*self.__item_quantity):
					self.__redeem_codes_list.append(self.generate_verification_code())
				self.__redeem_codes_list = sorted(set(self.__redeem_codes_list), key = self.__redeem_codes_list.index)
				for index,i in enumerate(range(0,len(self.__redeem_codes_list))):
					number = index%5
					self.__redeem_codes[self.generate_verification_code()] = number
				self.__save_config(game_name)
			self.__count = 60*60*24*30
			while self.__count!=0:
				self.__count-=1
				time.sleep(1)

	def __merge_dic(self,x,y):
		z = x.copy()
		z.update(y)
		return z

	def __save_config(self,game_name):
		all_codes = {}
		layer_list = {}
		for i in range(self.__item_quantity+1):
			layer_list[i]={}

		for index,code in enumerate(self.__redeem_codes):
			number = index%self.__item_quantity
			layer_list[number][code]=str(number)

		for i in range(self.__item_quantity):
			all_codes = self.__merge_dic(all_codes,layer_list[i])
		# all_codes = {**layer_list0, **layer_list1, **layer_list2, **layer_list3, **layer_list4, **layer_list5, **layer_list6, **layer_list7, **layer_list8, **layer_list9}

		with open(f"{self.__root_OperationLives}/{self.__reedem_codes_file}_{game_name}_V{self.__reedem_code_version}.json",mode='w',encoding="utf8") as file_context:
			all_codes_string = json.dumps(all_codes)
			file_context.write(all_codes_string)
		# print("all_codes="+str(all_codes))
		self.__all_redeem_codes[game_name]=all_codes
		self.__redeem_codes = dict()
		self.__redeem_codes_list = []


	async def redeem(self, game_name:str, redeem_code:str):
		if game_name not in self.__game_names:
			return self._message_typesetting(400,"error",{"status":"200","message":"don't have such name"})
		if  redeem_code not in self.__all_redeem_codes[game_name]:
			return self._message_typesetting(401,"error",{"status":"200","message":"don't have such redeem codes"})
		result = self.__all_redeem_codes[game_name][redeem_code]
		if result!=-1:
			self.__all_redeem_codes[game_name][redeem_code]=-1
			return self._message_typesetting(200,"redeem success",{"result":result})
		else:
			return self._message_typesetting(201,"redeem codes had been used",{"result":result})

	async def expiretime(self):
		m, s = divmod(self.__count, 60)
		h, m = divmod(m, 60)
		d, h = divmod(h, 24)
		return self._message_typesetting(200,"redeem success",{"time":"%02ddays:%02dhours:%02dminutes:%02dseconds" % (d, h, m, s)})

	async def function_hello(self, world: int, unique_id: str):
		# card_info = await self._execute_statement(world, f'select vip_card_type from player where unique_id="{unique_id}"')
		return self._message_typesetting(200,"this is message",{"status":"200","wtf":"a"})

	async def function_hello_noparam(self):
		# card_info = await self._execute_statement(world, f'select vip_card_type from player where unique_id="{unique_id}"')
		return self._message_typesetting(200,"this is message",{"status":"200","wtf":"a"})




ROUTES = web.RouteTableDef()


def _json_response(body: dict = "", **kwargs) -> web.Response:
	kwargs['body'] = json.dumps(body or kwargs['kwargs']).encode('utf-8')
	kwargs['content_type'] = 'text/json'
	return web.Response(**kwargs)



#json param, get result from request post
#http://localhost:9989/redeem
@ROUTES.post('/redeem')
async def _redeem(request: web.Request) -> web.Response:
	post = await request.post()
	print("post="+str(post))
	result = await (request.app['MANAGER']).redeem(post['gamename'], post['redeemcode'])
	return _json_response(result)

#no param, get result directly
#http://localhost:9989/expiretime
@ROUTES.get('/expiretime')
async def _expiretime(request: web.Request) -> web.Response:
	post = await request.post()
	result = await (request.app['MANAGER']).expiretime()
	return _json_response(result)

#json param, get result from request post
#http://localhost:9989/function_hello_json
@ROUTES.post('/function_hello_json')
async def _function_hello_json(request: web.Request) -> web.Response:
	post = await request.post()
	result = await (request.app['MANAGER']).function_hello(int(post['world']), post['unique_id'])
	return _json_response(result)


#json param, get result from request query
#http://localhost:9989/function_hello_query?world=0&unique_id=aabbaaaaaaaaa
@ROUTES.post('/function_hello_query')
async def _function_hello_query(request: web.Request) -> web.Response:
	query =  request.query
	result = await (request.app['MANAGER']).function_hello(int(query['world']), query['unique_id'])
	return _json_response(result)

#no param, get result directly
#http://localhost:9989/function_hello_noparam
@ROUTES.get('/function_hello_noparam')
async def _function_hello_noparam(request: web.Request) -> web.Response:
	post = await request.post()
	result = await (request.app['MANAGER']).function_hello_noparam()
	return _json_response(result)

def run():
	print("version:1.0")
	app = web.Application()
	app.add_routes(ROUTES)
	app['MANAGER'] = GameManager()
	web.run_app(app, port = "9989")


if __name__ == '__main__':
	run()
