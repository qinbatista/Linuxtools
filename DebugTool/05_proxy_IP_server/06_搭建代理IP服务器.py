import sys, os, platform
def get_desktop():
	return os.path.join(os.path.expanduser("~"), 'Desktop')
def PythonLocation():
	return os.path.dirname(os.path.realpath(__file__))
def main():
	os.system("apt-get -y install squid -y")
	os.system("cp "+PythonLocation()+"/squid.conf /etc/squid/squid.conf")
	os.system("service squid restart")
if __name__ == '__main__':
    main()