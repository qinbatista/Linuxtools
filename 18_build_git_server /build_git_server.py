import sys, os, platform
def get_desktop():
	return os.path.join(os.path.expanduser("~"), 'Desktop')
def PythonLocation():
	return os.path.dirname(os.path.realpath(__file__))

def change_shall_premssion(name):
	'''
	only git can shall to this user
	'''
	new_content = []
	with open("/etc/passwd",mode='r',encoding="utf8") as file:
		content =  file.readlines()
		for raw in content:
			if raw.find(name)!=-1:new_content.append(raw[:raw.rfind(":")]+":/usr/bin/git-shell")
			else:new_content.append(raw)
	with open("/etc/passwd",mode='w',encoding="utf8") as file:
		file.writelines(new_content)


def create_user():
	name = input("user name:")
	os.system("adduser "+name)
	os.system("su "+name)
	os.system("ssh-keygen")
	change_shall_premssion(name)

def list_user():
	'''
	nevigate to /home for finding all users
	'''
	file_name_lists = os.listdir('/home')
	for index, name in enumerate(file_name_lists):
		print(f'{index}:{name}')
	return file_name_lists[int(input('input your choice(integer only):'))]

def add_ssh_to_user(name, key):
	with open("/home/" + name + "/.ssh/authorized_keys", mode='a', encoding="utf8") as file:
		file.writelines(key)
	print(f'{name}/.ssh/authorized_keys added:{key}')

def main():
	print("1: create user")
	print("2: add ssh key to user")
	choice = input('input your choice:')
	if choice == '1':
		create_user()
	elif choice == '2':
		add_ssh_to_user(list_user(),input('input your ssh public key:'))
	else:
		print("exit")

if __name__ == '__main__':
	main()