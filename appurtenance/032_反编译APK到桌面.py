import sys, os, platform
import PythonFunction

def main():
	_Path = sys.argv[1]
	#_Path = "C:\\Users\\qinyupeng\\Desktop\\GameAPK\\afs.waf.aaf1.apk"
	PythonFunction.FuncCommon.DecompileAPKCall(_Path)

if __name__ == '__main__':
    main()