import sys, os, platform
def get_desktop():
	return os.path.join(os.path.expanduser("~"), 'Desktop')
def main():
	#_Path = sys.argv[1]
	#_Path = r"C:\Users\qinba\Desktop\GoldenGoalSoccer_Base_baidu_N1.3.7_C52310_2018_05_18_15_00_27.apk"
	print("Input your Web:")
	MyPackageName = input()
	os.system("youtube-dl -f 22  --proxy 'socks5://127.0.0.1:1080' "+ MyPackageName+" --external-downloader aria2c --external-downloader-args \"-x 16 -k 1M\"")
if __name__ == '__main__':
    main()