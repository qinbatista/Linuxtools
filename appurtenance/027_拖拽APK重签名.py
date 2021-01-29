import sys, os, platform
import PythonFunction

def main():
	_path = sys.argv[1]
	#_path = r"C:\Users\qinba\Desktop\GiveItUp_Base.apk"
	print("Input keystore path:")
	_KeyPath = input()
	PythonFunction.FuncCommon.Resgin(_path,_KeyPath)

if __name__ == '__main__':
    main()