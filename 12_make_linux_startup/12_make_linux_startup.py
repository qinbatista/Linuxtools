import sys, os, platform
def get_desktop():
	return os.path.join(os.path.expanduser("~"), 'Desktop')
def main():
	# pip3 install youtube-dl
	print("Input your iso:")
	MyPackageName = input()
	os.system("diskutil unmountDisk /dev/disk2")
	os.system("sudo dd if="+MyPackageName+" of=/dev/disk2 bs=2m")
if __name__ == '__main__':
	#sudo dd if=/Users/batista/Desktop/ubuntu-18.04.3-live-server-amd64.iso of=/dev/disk2 bs=2m
	
    main()