import sys, os, platform
import pymysql
def get_desktop():
	return os.path.join(os.path.expanduser("~"), 'Desktop')
def PythonLocation():
	return os.path.dirname(os.path.realpath(__file__))
def DeployMySQL():
	os.system("apt-get -y install mysql-server")
	os.system("wget https://bootstrap.pypa.io/get-pip.py")
	os.system("python3  get-pip.py")
	os.system("pip3 install pymysql")
	os.system("cp "+PythonLocation()+"/50-server.cnf /etc/mysql/mariadb.conf.d/50-server.cnf")
	os.system("mysql")
	#os.system("grant all privileges on *.* to 'root'@'%' identified by 'a123456.';")# *.* 表示可以访问的表格第一个*表示数据库，第二个*表示数据表 root表示用户名可以随意修改，%表示所有ip均可访问，也可以指定ip，a123456.表示密码
	#os.system("flush privileges;")
	os.system("/etc/init.d/mysql start")
def ConnectSQL():
	#!/usr/bin/python3
	#打开数据库连接
	db = pymysql.connect("202.182.96.131","root","a123456.","MagicWandAIWeb" )
	# 使用 cursor() 方法创建一个游标对象 cursor
	cursor = db.cursor()
	# 使用 execute()  方法执行 SQL 查询 
	cursor.execute("SELECT VERSION()")
	# 使用 fetchone() 方法获取单条数据.
	data = cursor.fetchone()
	print ("Database version : %s " % data)
	# 关闭数据库连接
	db.close()
def main():
	# DeployMySQL()
	ConnectSQL()
	pass
if __name__ == '__main__':
    main()