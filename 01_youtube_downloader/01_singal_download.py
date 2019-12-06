import sys, os, platform
def get_desktop():
	return os.path.join(os.path.expanduser("~"), 'Desktop')
def main():
	# pip3 install youtube-dl
	print("Input your Web:")
	MyPackageName = input()
	os.system("youtube-dl --write-sub --all-subs "+ MyPackageName)
if __name__ == '__main__':
    main()