import sys, os, platform
import PythonFunction

def main():
	print("Input your package name:")
	MyPackageName = input()
	print("MyPackageName="+MyPackageName)
	PythonFunction.FuncCommon.GetNULLPackage(MyPackageName)
	print("Press any keys to exit...")
if __name__ == '__main__':
    main()