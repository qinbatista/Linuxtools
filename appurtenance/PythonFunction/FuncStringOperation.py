import sys, os, platform
import os
import time
import shutil
import chardet
import sys,os

def UsePlatform():
	sysstr = platform.system()
	if(sysstr =="Windows"):
		return "Windows"
	elif(sysstr == "Linux"):
		return "Linux"
	else:
		return "Mac"

def CheckSensitiveWord(KeyWord,Location):
	if UsePlatform()=="Windows":
		RegistDragPromission()
	CompareKeyWord(KeyWord,Location)
def RegistDragPromission():
	#print(os.path.abspath('.')+"/PythonRegedit.reg")
	if(os.path.isfile(os.path.abspath('.')+"/PythonRegedit.reg")==True):
		return
	#print("Current:"+os.getcwd())
	os.chdir(r''+"PythonFunction/__pycache__")
	#print("current:"+os.getcwd())
	if os.path.isfile("PythonRegedit.reg") == False:
		os.chdir(r"../")
		os.system("PythonRegedit.reg")
		shutil.copy(os.path.abspath('.')+"/PythonRegedit.reg",os.path.abspath('.')+"/__pycache__/PythonRegedit.reg")
def GetMyData(Location):
	file_object = open(Location,encoding="utf8")
	all_the_text=[]
	try:
		all_the_text = file_object.readlines()
	finally:
		file_object.close( )
	return all_the_text

def GetData():
	if os.path.isfile(sys.path[0]+"/PythonFunction/SensitiveVocabulary.txt"):
		file_object = open(sys.path[0]+"/PythonFunction/SensitiveVocabulary.txt",encoding="utf8")
	line = file_object.readline()
	all_the_text=[]
	try:
		while line:
			line = line.replace(" ","")
			ListLine = line.split('、')
			for i in ListLine:
				all_the_text.append(i)
			#print(all_the_text)
			line = file_object.readline()
	finally:
		file_object.close( )
	return all_the_text
def CompareKeyWord(KeyWord,Location):
	myfile = open(Location,'rb')
	data = myfile.read()
	di= chardet.detect(data)
	myfile.close()
	if di["encoding"]!="utf-8" and di["encoding"]!="UTF-8-SIG" :
		print(Location+"↓\nIt is not UTF-8 format, please swithc text format as UTF-8"+", your mode is "+di["encoding"])
		input()
	DataList = GetData()
	MyDataList = GetMyData(Location)
	
	CountLine= 0
	if(KeyWord=="Chinese"):
		for i in MyDataList:
			for j in DataList:
				if j in i:
					if(i!="\n" and j!="\n" and i!="" and j!="" and i!= None and j!= None):
						print("Line ["+str(CountLine)+"] found sensitive context:"+j+"->your context:"+i)
						break
			CountLine+=1
	if(KeyWord=="English"):
		DataList1=[chr(i) for i in range(97,123)]
		DataList2=[chr(i) for i in range(65,91)]
		for my in DataList2:
			DataList1.append(my)
		#print(DataList1)
		for i in MyDataList:
			for j in DataList1:
				if j in i:
					#if(i!="\n" and j!="\n" and i!="" and j!="" and i!= None and j!= None):
					print("Line ["+str(CountLine)+"] found sensitive context:"+j+"->your context:"+i)
					break
			CountLine+=1
def main():
	#ChangeDemoPackageName(os.path.abspath('.')+"/../DemoProject/"+"02_ChannelDemo"+"Copy"+"/src/com/east2west/testapp/MainActivity.java",ReadXml_GetPackageName(os.path.abspath('.')+"/../DemoProject/"+"02_ChannelDemo"+"Copy"+"/AndroidManifest.xml"))
	#input()
	#print(ReadXml_GetPackageName(os.path.abspath('.')+"/../DemoProject/"+"02_ChannelDemo"+"Copy"+"/AndroidManifest.xml"))
	pass
if __name__ == '__main__':
    main()