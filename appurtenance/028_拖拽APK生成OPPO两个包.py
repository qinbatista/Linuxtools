import sys, os, platform
import PythonFunction

def main():
	_path = sys.argv[1]
	#_path = r"C:\Users\qinba\Desktop\GiveItUp_Base.apk"
	PythonFunction.FuncCommon.CreateOppo(_path)

if __name__ == '__main__':
    main()