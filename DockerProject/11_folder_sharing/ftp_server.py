from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


def run():
# 	实例化DummyAuthorizer来创建ftp用户
	authorizer = DummyAuthorizer()
	# 参数：用户名，密码，目录，权限
	authorizer.add_user('user', '12345', '/Users/batista/Desktop', perm='elradfmwMT')
	# 匿名登录
	# authorizer.add_anonymous('/home/nobody')
	handler = FTPHandler
	handler.authorizer = authorizer
	# 参数：IP，端口，handler
	server = FTPServer(('', 9988), handler)
	server.serve_forever()


if __name__ == '__main__':
	run()
