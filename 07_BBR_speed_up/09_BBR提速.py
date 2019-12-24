import sys, os, platform
def get_desktop():
	return os.path.join(os.path.expanduser("~"), 'Desktop')
def main():
	# pip3 install youtube-dl
	os.system("wget --no-check-certificate https://github.com/tcp-nanqinlang/general/releases/download/3.4.2.1/tcp_nanqinlang-fool-1.3.0.sh")
	if os.path.exists("tcp_nanqinlang-fool-1.3.0.sh"):
		os.system("bash tcp_nanqinlang-fool-1.3.0.sh")
	else:
		os.system("bash install.sh")
if __name__ == '__main__':
    main()