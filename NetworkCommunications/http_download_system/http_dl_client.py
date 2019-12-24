# modified fetch function with semaphore
import random
import asyncio
from aiohttp import ClientSession
import aiohttp
from datetime import datetime
import time
import numpy as np
class httpClient(object):
	def __init__(self,urls:list=[], params:list = []):
		self._urls = urls
		self._params = params
		self.result= []
		self.requst_type = -1
		self.is_post=0
		self.is_get=0

	async def __run(self):
		tasks = []
		sem = asyncio.Semaphore(1000)
		timeout = aiohttp.ClientTimeout(total=10)
		async with ClientSession(timeout=timeout) as session:
			self.__analysis_url_param()
			for index, url in enumerate(self._urls):
				task = asyncio.ensure_future(self.__bound_fetch(sem, url,self._params[index],session))
				tasks.append(task)
			self.result = await asyncio.gather(*tasks)

	async def __fetch(self, url, param, session):
		try:
			if param=={}:
				async with session.get(url) as response:
					# print(response.status)
					# print(await response.text())
					return await response.text("utf-8")
			else:
				async with session.post(url, data=param) as response:
					# print(response.status)
					# print(await response.text())
					return await response.text("utf-8")
		except:
			return "timeout:"+url

	async def __bound_fetch(self, sem, url,param, session):
		async with sem:
			return await self.__fetch(url, param, session)

	def __analysis_url_param(self):
		for index, checkurl in enumerate(self._urls):
			self._urls[index] = self.__check_url(checkurl)

	def __check_url(self,url):
		if url.find("http")==-1:return f"http://{url}"
		else:return url

	def access(self):
		start = time.time()
		self.requst_type = self.is_get
		loop = asyncio.get_event_loop()
		future = asyncio.ensure_future(self.__run())
		loop.run_until_complete(future)
		end = time.time()
		print(f"\033[1;93m[urls:{len(self._urls)}]\033[0m\033[1;93m{'cost time:'}\033[0m\033[1;92m{(format(end-start,'0.4f'))}\033[0m")
		return self.result

if __name__ == "__main__":

	my_requests = np.array([
		['182.92.1.245:9988/function_hello',{"world":0,"unique_id":"aabb"}] for _ in range(1)
		# ['localhost:9988/function_hello',{"world":0,"unique_id":"aabb"}] for _ in range(1)
		])
	# my_requests_addition = np.array([['www.bing.com',{}] for _ in range(1)])
	# all_requests = np.concatenate((my_requests,my_requests_addition))

	myurls = my_requests[:,0]
	myparams =my_requests[:,1]
	hc = httpClient(urls = myurls,params = myparams)
	result = hc.access()
	print(str(result))

