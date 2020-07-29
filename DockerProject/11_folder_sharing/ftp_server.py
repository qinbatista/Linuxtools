from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
class FtpManager:
	def __init__(self, worlds = []):
		self.__reedem_codes_file = 'redeem'
		self.__download_folder = "/Users/batista/Desktop/" #~/download_folder/

	def	__list_folder(self, _path):
		List = []
		for i in os.listdir(_path):
			List.append(i)
		return List

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

	def create_file(self,_path,_context):
		with open(_path,mode='w',encoding="utf8") as file_context:
			file_context.write(_context)
	def start_server(self):
		folder_name = self.__list_folder(self.__download_folder)
		print("folder_name="+folder_name)
		#实例化DummyAuthorizer来创建ftp用户
		authorizer = DummyAuthorizer()
		for my_name in folder_name:
		# 参数：用户名，密码，目录，权限
			os.mkdir(self.__download_folder+"/"+my_name)
			my_password = self.generate_verification_code()
			print(f"create usersname:{my_name},password:{my_password},path_name:{self.__download_folder+my_name}")
			authorizer.add_user(my_name, my_password, self.__download_folder+my_name, perm='elradfmwMT')
		# 匿名登录
		# authorizer.add_anonymous('/home/nobody')
		handler = FTPHandler
		handler.authorizer = authorizer
		# 参数：IP，端口，handler
		server = FTPServer(('', 9988), handler)
		server.serve_forever()


if __name__ == '__main__':
	my_ftp = FtpManager()
	my_ftp.start_server()