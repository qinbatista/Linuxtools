import sys, os, platform
import PythonFunction

def main():


	PythonFunction.FuncStringOperation.CheckSensitiveWord("Chinese",sys.argv[1])
	print("Press any keys to exit...")
	input()
if __name__ == '__main__':
    main()