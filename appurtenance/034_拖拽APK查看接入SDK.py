import sys, os, platform
import PythonFunction

def main():
	_Path = sys.argv[1]
	#_Path = "C:\\Users\\qinyupeng\\Desktop\\GameAPK\\game-release_cuizi20180413_20180416163900.apk"
	PythonFunction.FuncCommon.CheckAPKContainedSDK(_Path)
if __name__ == '__main__':
    main()