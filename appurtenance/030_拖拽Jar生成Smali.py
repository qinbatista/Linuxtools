import sys, os, platform
import PythonFunction

def main():
	
	#CheckString = r"C:\Users\qinba\Desktop\bsgamedatasdk_android_library_1.0.6.jar"
	CheckString = sys.argv[1]
	#PythonFunction.FuncCommon.GetSmaliOfJar(sys.argv[1])
	getstring =  CheckString[CheckString.rfind(".")+1:]
	#print(getstring)
	if(getstring == "jar"):
		print("CheckString="+CheckString)
		PythonFunction.FuncCommon.GetSmaliOfJar(CheckString)
	else:
		print("Please drag .jar files.")
		input()
if __name__ == '__main__':
    main()