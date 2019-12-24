import sys, os, platform
def get_desktop():
	return os.path.join(os.path.expanduser("~"), 'Desktop')
def PythonLocation():
	return os.path.dirname(os.path.realpath(__file__))
def main():
	os.system("apt-get -y install shadowsocks")
	os.system("cp "+PythonLocation()+"/config.json /etc/shadowsocks/config.json")
	os.system("service shadowsocks restart")
if __name__ == '__main__':
    main()