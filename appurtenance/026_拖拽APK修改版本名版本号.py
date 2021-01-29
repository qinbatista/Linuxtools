import sys, os, platform
import PythonFunction

def main():

	print("VersionName:")
	VersionName=0
	VersionName = input()

	print("VersionCode:")
	VersionCode=0
	while True:
		VersionCode = input()
		if VersionCode.isdigit():
			break
		print("Please input number")
	_path = sys.argv[1]
	#_path = r"C:\Users\qinba\Desktop\GiveItUp_Base.apk"
	PythonFunction.FuncCommon.CheckVCVN(_path,VersionName,VersionCode)
	print("Press any keys to exit...")
if __name__ == '__main__':
    main()