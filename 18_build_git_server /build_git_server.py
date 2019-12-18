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
	change_shall_premssion(name)

def list_user():
	'''
	nevigate to /home for finding all users
	'''
	file_name_lists = os.listdir('/home')
	for index, name in enumerate(file_name_lists):
		print(f'[{index}]\t{name}')
	return file_name_lists[int(input('input your choice(integer only):'))]

def add_ssh_to_user(name, key):
	if os.path.exists("/home/" + name + "/.ssh/")==False:os.system("mkdir "+"/home/" + name + "/.ssh/")
	if os.path.exists("/home/" + name + "/.ssh/")==False:os.system("touch authorized_keys")
	os.system('chmod 700 ~/.ssh/')
	os.system('chmod 600 ~/.ssh/*')
	with open("/home/" + name + "/.ssh/authorized_keys", mode='a', encoding="utf8") as file:
		file.writelines(key+"\n")
	print(f'/home/{name}/.ssh/authorized_keys added:{key}')

def create_git_repositories(repositories):
	name = list_user()
	if os.path.exists("/home/" + name + "/.ssh/")==False:os.system('mkdir /'+ name)
	os.system('chown '+name+' /'+ name+"/")
	os.system('chmod 700 /'+ name+"/")
	os.system('git init --bare '+'/'+name+'/'+repositories+'.git')
	print(f'[success]\tgit clone ssh://{name}@remote2.magicwandai.com:10022/{name}/{repositories}.git')

def main():
	while True:
		print("[1]\tcreate user")
		print("[2]\tadd ssh key to user")
		print("[3]\tcreate a repositories")
		choice = input('input your choice:')
		if choice == '1':
			create_user()
		elif choice == '2':
			add_ssh_to_user(list_user(),input('input your ssh public key:'))
		elif choice =='3':
			create_git_repositories(input('input repositories name:'))
		else:
			print("exit")
			break

if __name__ == '__main__':
	main()