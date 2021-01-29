import sys, os, platform
import PythonFunction

def main():
	print("Input your ChannelName:")
	ChannelName = input()
	_path = sys.argv[1]
	#_path = r"C:\Users\qinba\Desktop\GiveItUp_Base.apk"
	PythonFunction.FuncCommon.CheckAPKChannelName(_path,ChannelName)
if __name__ == '__main__':
    main()