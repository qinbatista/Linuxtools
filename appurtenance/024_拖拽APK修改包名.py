import sys, os, platform
import PythonFunction

def main():
	print("Input your package name:")
	MyPackageName = input()
	_path = sys.argv[1]
	#_path = r"C:\Users\qinba\Desktop\GiveItUp_Base.apk"
	PythonFunction.FuncCommon.CheckAPKPackageName(_path,MyPackageName)
	print("Press any keys to exit...")
if __name__ == '__main__':
    main()