import sys, os, platform
import PythonFunction

def main():

	print("Input CPS number:")
	num=0
	while True:
		num = input()
		if num.isdigit():
			break
	print("Input keysotre Location:")
	while True:
		key = input()
		if key!="":
			break
	_path = sys.argv[1]

	#_path = r"C:\Users\qinba\Desktop\GiveItUp_Base.apk"
	PythonFunction.FuncCPSOperation.CreateCPS(num,_path,key)
	print("Press any keys to exit...")
if __name__ == '__main__':
    main()