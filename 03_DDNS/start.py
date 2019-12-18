import sys, os
if __name__ == '__main__':
	print("[1]\t deploy Server")
	print("[2]\t deploy Client")
	choice = input('Input your choice:')
	if choice == '1':
		os.system('python3 ./01_Server.py')
	elif choice =='2':
		os.system('python3 ./02_Client.py')
	else:
		print("closed!")