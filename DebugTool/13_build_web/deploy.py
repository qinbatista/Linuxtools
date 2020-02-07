import sys, os
import socket
import threading
from time import ctime

def DeployServer():
	os.chdir(os.path.abspath(os.path.dirname(__file__)))
	os.system("pwd")
	web_path = "singmaan_web"
	os.system("git clone https://qinbatista:qinyupeng1@bitbucket.org/qinbatista/singmaan_web.git")
	os.system("apt-get update")
	os.system("apt-get -y install apache2")
	os.system("cp -rf "+web_path+" /var/www/")
	folder_name = web_path[web_path.rfind('/')+1:]
	os.system("mv /var/www/"+folder_name+" /var/www/website")
	os.system("cp 000-default.conf /etc/apache2/sites-available/000-default.conf")
	os.system("/etc/init.d/apache2 restart")

if __name__ == '__main__':
	DeployServer()