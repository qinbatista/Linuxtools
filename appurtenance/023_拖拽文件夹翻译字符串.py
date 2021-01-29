import sys, os, platform
import PythonFunction

def main():
	_path = sys.argv[1]
	#_path = r"C:\Users\qinba\Desktop\languages"
	PythonFunction.FuncCommon.Translate(_path)
	print("Press any keys to exit...")
	input()
if __name__ == '__main__':
    main()