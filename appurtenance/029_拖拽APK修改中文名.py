import sys, os, platform
import PythonFunction

def main():
	print("Input your Chinese name:")
	MyPackageName = input()
	_Path = sys.argv[1]
	#_Path = r"C:\Users\qinba\Desktop\GiveItUp_Base.apk"
	PythonFunction.FuncCommon.CheckAPKChineseName(_Path,MyPackageName)

if __name__ == '__main__':
    main()