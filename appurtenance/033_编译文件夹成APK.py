import sys, os, platform
import PythonFunction

def main():
	_Path = sys.argv[1]
	#_Path = r"C:\Users\qinba\Desktop\GiveItUp_Base"
	PythonFunction.FuncCommon.CompileAPKCall(_Path)

if __name__ == '__main__':
    main()