import sys, os
import socket
import threading
from time import ctime
def main():
	os.system('service ssh start')
	while True:
		new_ssh = input('input your id_rsa.pub:')
		os.system('echo '+new_ssh+'>>~/.ssh/authorized_keys')
if __name__ == '__main__':
    main()