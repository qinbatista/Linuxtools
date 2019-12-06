import sys, os
import socket
import threading
from time import ctime

def DeployServer():
	'''#must excute before
	apt-get update && apt-get -y install python3 git && git clone https://qinbatista:qinyupeng1@bitbucket.org/qinbatista/magicwandaisample.git && cd magicwandaisample/13_docker_server && python3 docker_server.py
	'''
	os.chdir(os.getcwd())
	os.system("apt-get -y install python aria2 screen ssh iptraf make gcc sudo vim iptraf wget curl proxychains locales")

	os.system("git clone http://git.mrwang.pw/Reed/Linux_ssr_script.git")
	os.system("cd Linux_ssr_script && chmod +x ./ssr")
	os.chdir(os.getcwd()+"/Linux_ssr_script")
	os.system("sudo mv ./ssr /usr/local/sbin/")
	os.system("ssr install")
	os.chdir(os.getcwd()+"/../")
	os.system("cp config.json /root/.local/share/shadowsocksr/config.json")
	os.system("cp sshd_config /root/ssh/sshd_config")
	os.system("cp proxychains.conf /etc/proxychains.conf")
	os.system("wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate")
	os.system("python3 get-pip.py")
	os.system("pip3 install youtube-dl")
	os.system("wget https://github.com/jedisct1/libsodium/releases/download/1.0.10/libsodium-1.0.10.tar.gz")
	os.system("tar xzvf libsodium-1.0.10.tar.gz")
	os.chdir(os.getcwd()+"/libsodium-1.0.10")
	os.system("./configure")
	os.system("make -j8 && make install")
	os.system("echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf")
	os.system("ldconfig")
	os.chdir(os.getcwd()+"/../")
	os.system("dpkg-reconfigure locales 471 472 473")


def main():
	DeployServer()
if __name__ == '__main__':
    main()