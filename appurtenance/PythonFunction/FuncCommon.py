#encoding=utf8
import sys, os, platform
import os
import time
import shutil
import chardet
import sys,os
import xml.dom.minidom
import zipfile
import urllib.request
import random
import json
import xml.dom.minidom
import unicodedata
import re
from subprocess import Popen, PIPE, STDOUT
CallMethodPath=""
PythonVersion = ""
copyFileCounts = 0
def GetPythonCommand():
	global PythonVersion
	if PythonVersion!="":
		return PythonVersion
	version1 = os.popen("python3 --version")
	version2 = os.popen("python.exe --version")
	version3 = os.popen("python --version")
	# print("Version:"+version1.read())
	# print("show:"+version2.read())
	# print("show:"+version3.read())
	if version1.read()!="":
		PythonVersion="python3"
	if version2.read()!="":
		PythonVersion="python.exe"
	if version3.read()!="":
		PythonVersion="python"
	print("Your are using python command:"+PythonVersion)
	return PythonVersion
def UsePlatform(arg):
	def UsePlatformfunc(FunctionName):
		def UsePlatformfunc_in(*args,**kwargs):
			sysstr = platform.system()
			MyList = FindAllInFolder(os.path.dirname(os.path.realpath(__file__))+"/__pycache__")
			for i in MyList:
				if ".pyc" in i:
					continue
				if "PythonRegedit.reg" in i:
					continue
				if "." not in i :
					DeleteFolder(i)
				else: 
					if os.path.isfile(i):
						os.remove(i)
					if os.path.isdir(i):
						DeleteFolder(i)
			if(sysstr =="Windows"):
				if arg=="Windows":
					return FunctionName(*args,**kwargs)
				else:
					print("This is not your requied Platform")
					return False
			elif(sysstr == "Linux"):
				if arg=="Linux":
					return FunctionName(*args,**kwargs)
				else:
					print("This is not your requied Platform")
					return False
			elif(sysstr == "Darwin"):
				return FunctionName(*args,**kwargs)
			else:
				print("This is not your requied Platform")
				return False
			return FunctionName(*args,**kwargs)
		return UsePlatformfunc_in
	return UsePlatformfunc

def FindAllInFolder(_path):
	ListMyFolder = []
	for filename in os.listdir(_path):
		ListMyFolder.append(_path+"/"+filename)
	return ListMyFolder

def RegistDragPromission(arg):
	def RegistDragPromissionfunc(FunctionName):
		def RegistDragPromissionfunc_in(*args,**kwargs):
			sysstr = platform.system()
			if "DragPromission" == arg and sysstr == "Windows":
				#print("Enter:"+PythonLocation())
				#print(CallMethodPath)
				if(os.path.isfile(PythonLocation()+"/PythonRegedit.reg")==False):
					print("Can't find "+PythonLocation()+"/PythonRegedit.reg")
					return False
				if os.path.isfile(PythonLocation()+"/__pycache__/PythonRegedit.reg") == False:
					os.system(PythonLocation()+"/"+"PythonRegedit.reg")
					shutil.copy(PythonLocation()+"/PythonRegedit.reg",PythonLocation()+"/__pycache__/PythonRegedit.reg")
					os.chdir(CallMethodPath)
					return FunctionName(*args,**kwargs)
				else:
					os.chdir(CallMethodPath)
					return FunctionName(*args,**kwargs)
			else:
				return FunctionName(*args,**kwargs)
		return RegistDragPromissionfunc_in
	return RegistDragPromissionfunc

def CallMethodLocation(arg):
	def CallMethodLocationfunc(FunctionName):
		def CallMethodLocationfunc_in(*args,**kwargs):
			global CallMethodPath
			CallMethodPath = os.path.abspath('.')
			ret = FunctionName(*args,**kwargs)
			return ret
		return CallMethodLocationfunc_in
	return CallMethodLocationfunc

def CheckIfHaveSignature(_CheckLocation):
	APKname = _CheckLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	os.chdir(r''+PythonLocation()+"/__pycache__")
	if os.path.exists(os.path.abspath('.')+"/assets"):
		DeleteFolder(os.path.abspath('.')+"/assets")
	if os.path.exists(os.path.abspath('.')+"/META-INF"):
		DeleteFolder(os.path.abspath('.')+"/META-INF")
	if os.path.exists(os.path.abspath('.')+"/res"):
		DeleteFolder(os.path.abspath('.')+"/res")
	if os.path.exists(os.path.abspath('.')+"/AndroidManifest.xml"):
		DeleteFolder(os.path.abspath('.')+"/AndroidManifest.xml")
	if os.path.exists(os.path.abspath('.')+"/classes.dex"):
		DeleteFolder(os.path.abspath('.')+"/classes.dex")
	if os.path.exists(os.path.abspath('.')+"/resources.arsc"):
		DeleteFolder(os.path.abspath('.')+"/resources.arsc")
	if os.path.exists(os.path.abspath('.')+"/copy.apk"):
		DeleteFolder(os.path.abspath('.')+"/copy.apk")
	if os.path.exists(os.path.abspath('.')+"/copy_signed.apk"):
		DeleteFolder(os.path.abspath('.')+"/copy_signed.apk")
	if os.path.exists(os.path.abspath('.')+"/"+foldername):
		DeleteFolder(os.path.abspath('.')+"/"+foldername)
	#print("jar xf "+_CheckLocation)
	os.system("jar xf "+_CheckLocation)
	if os.path.exists(os.path.abspath('.')+"/META-INF"):
		#print("[Python Notice] Please delete android signature and try again(delete /META-INF folder)")
		return False
	os.chdir(r''+CallMethodPath)
	return True

def PythonLocation():
	return os.path.dirname(os.path.realpath(__file__))

def DecopileAPK(_APKLocation):
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	if os.path.exists(PythonLocation()+"/__pycache__"+"/"+foldername):
		DeleteFolder(PythonLocation()+"/__pycache__"+"/"+foldername)
	os.chdir(r''+PythonLocation()+"/__pycache__")
	os.system(PythonLocation()+"/../Tool/apktool d "+_APKLocation)
	os.chdir(r''+CallMethodPath)
def RebuildAPK(_APKLocation):
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	# foldername=APKname[:PointCount]
	APKname[:PointCount]
	os.chdir(r''+PythonLocation()+"/__pycache__")
	os.system(PythonLocation()+"/../Tool/apktool b "+_APKLocation)
	os.chdir(r''+CallMethodPath)
def Unzip(_APKLocation):
	os.chdir(r''+PythonLocation()+"/__pycache__")
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	# foldername=APKname[:PointCount]
	APKname[:PointCount]
	if os.path.exists(PythonLocation()+"/__pycache__/foldername"):
		DeleteFolder(PythonLocation()+"/__pycache__/foldername")
	if os.path.exists(PythonLocation()+"/__pycache__/assets"):
		DeleteFolder(PythonLocation()+"/__pycache__/assets")
	if os.path.exists(PythonLocation()+"/__pycache__/META-INF"):
		DeleteFolder(PythonLocation()+"/__pycache__/META-INF")
	if os.path.exists(PythonLocation()+"/__pycache__/res"):
		DeleteFolder(PythonLocation()+"/__pycache__/res")
	if os.path.isfile(PythonLocation()+"/__pycache__/AndroidManifest.xml"):
		os.remove(PythonLocation()+"/__pycache__/AndroidManifest.xml")
	if os.path.isfile(PythonLocation()+"/__pycache__/classes.dex"):
		os.remove(PythonLocation()+"/__pycache__/classes.dex")
	if os.path.isfile(PythonLocation()+"/__pycache__/resources.arsc"):
		os.remove(PythonLocation()+"/__pycache__/resources.arsc")
	#print("jar xf "+_APKLocation)
	os.system("jar xf "+_APKLocation)
	os.chdir(r''+CallMethodPath)

def SignatureCommond(_APKLocation):
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	# foldername=APKname[:PointCount]
	APKname[:PointCount]
	if os.path.exists(PythonLocation()+"/__pycache__/META-INF")==False:
		print("Your APK don't have META-INF folder")
		return
	MySignature = ListFolder(PythonLocation()+"/__pycache__/META-INF")
	for name in MySignature:
		if ".RSA" in name:
			os.system("keytool -printcert -file "+PythonLocation()+"/__pycache__/META-INF/"+name)

def ChangePackageName(_APKLocation,_PackageName):
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	_Path = PythonLocation()+"/__pycache__/"+foldername+"/AndroidManifest.xml"
	dom = xml.dom.minidom.parse(_Path)
	root = dom.documentElement
	root.setAttribute("package",_PackageName)
	try:
		with open(_Path,'w',encoding='UTF-8') as _Path:
			dom.writexml(_Path,indent='',addindent='',newl='',encoding='UTF-8')
	except Exception as err:
		print("ERROR[{0}".format(err))

def SetGradlePackageName(_Location,_PackageName):
	if os.path.isfile(_Location):
		file_object = open(_Location,encoding="utf8")
	JavaCode=[]

	try:
		all_the_text = file_object.readlines()
		for i in all_the_text:
			if(i.find("applicationId")!=-1):
				newString = i.replace("game.east2west.com.myapplication",_PackageName)
				JavaCode.append(newString)
				pass
			else:
				JavaCode.append(i)
	finally:
		file_object.close()
	file_object_read = open(_Location,'w',encoding="utf-8")
	try:
		file_object_read.writelines(JavaCode)
	finally:
		file_object_read.close( )

def GetPackageName(_APKLocation):
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	_Path = PythonLocation()+"/__pycache__/"+foldername+"/AndroidManifest.xml"
	#print("--------------"+_Path)
	dom = xml.dom.minidom.parse(_Path)
	root = dom.documentElement
	stringForTem = root.getAttribute("package")
	return stringForTem

def GetPackageE2WNumber(_APKLocation):
	_APKLocation = _APKLocation.replace("\\","/")
	_Path=_APKLocation
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	dom = xml.dom.minidom.parse(PythonLocation()+"/__pycache__/"+foldername+"/AndroidManifest.xml")
	root = dom.documentElement
	#name =root.getAttribute("package")
	name  = root.getElementsByTagName("meta-data")
	global FoundKey
	nameofvalue=""
	FoundKey=False
	for node in name:
		nameofname = node.getAttribute("android:name")
		if nameofname=="E2W_NUMBER":
			nameofvalue = node.getAttribute("android:value")
			FoundKey=True
	if FoundKey==False:
		print("[ERROR] Can't find E2W_NUMBER")
	return nameofvalue
def Get_METE(_APKLocation,Key):
	_APKLocation = _APKLocation.replace("\\","/")
	_Path=_APKLocation
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	dom = xml.dom.minidom.parse(PythonLocation()+"/__pycache__/"+foldername+"/AndroidManifest.xml")
	root = dom.documentElement
	#name =root.getAttribute("package")
	name  = root.getElementsByTagName("meta-data")
	global FoundKey
	nameofvalue=""
	FoundKey=False
	for node in name:
		nameofname = node.getAttribute("android:name")
		if nameofname==Key:
			nameofvalue = node.getAttribute("android:value")
			FoundKey=True
	if FoundKey==False:
		print("[ERROR] Can't find "+Key)
	return nameofvalue
def GetVCVN(_APKLocation):
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	_Path = PythonLocation()+"/__pycache__/"+foldername+"/apktool.yml"
	StringList = []
	if os.path.isfile(_Path):
		file_object = open(_Path,encoding="utf8")
		try:
			all_the_text = file_object.readlines()
			for i in all_the_text:
				if "versionCode" in i:
					StringList.append(i)
				if "versionName" in i:
					StringList.append(i)
		finally:
			file_object.close( )
	return StringList

def CopyEmptyDemo(_Number):
	count = 1
	while True:
		if os.path.exists(PythonLocation()+"/__pycache__/"+"EmptyDemo"+str(count)):
			count+=1
		else:
			break
	CopyFiles(PythonLocation()+"/../Appurtenance/DemoAPK",PythonLocation()+"/__pycache__/"+"EmptyDemo"+str(count))
	return "EmptyDemo"+str(count)

def CopySDKToFolder(_ChannelName,SDKFolder):
	print(PythonLocation()+"/../channelsdk/ChannelSDK/"+_ChannelName.lower())
	if _ChannelName=="" or os.path.exists(PythonLocation()+"/../channelsdk/ChannelSDK/"+_ChannelName.lower()) == False:
		print("make sure your channel is exist:"+_ChannelName)
		return
	os.chdir(r''+PythonLocation()+"/__pycache__")
	if os.path.exists(PythonLocation()+"/../channelsdk/ChannelSDK/"+_ChannelName.lower()):
		CopyFiles(PythonLocation()+"/../channelsdk/ChannelSDK/"+_ChannelName.lower(),PythonLocation()+"/__pycache__/"+SDKFolder)
	os.chdir(r''+SDKFolder)
	os.system("android update project --name game -p ./")
	os.system("ant clean")
	os.system("ant release")
	os.chdir(r''+CallMethodPath)
def DecompileSDKAPK(SDKFolder,_ChannelName):
	os.chdir(r''+PythonLocation()+"/__pycache__/"+SDKFolder+"/bin")
	#print(PythonLocation()+"/../../03_Appurtenance/Tool/apktool d "+_APKLocation)
	os.system(PythonLocation()+"/../Tool/apktool d "+PythonLocation()+"/__pycache__/"+SDKFolder+"/bin/app-release.apk")
	
	if os.path.exists(PythonLocation()+"/__pycache__/"+SDKFolder+"/bin/app-release/assets"):
		if os.path.exists(PythonLocation()+"/../../02_ChannelSdk/ChannelSDKSmali/"+_ChannelName+"/assets"):
			DeleteFolder(PythonLocation()+"/../../02_ChannelSdk/ChannelSDKSmali/"+_ChannelName+"/assets")
		CopyFiles(PythonLocation()+"/__pycache__/"+SDKFolder+"/bin/app-release/assets",PythonLocation()+"/../../02_ChannelSdk/ChannelSDKSmali/"+_ChannelName+"/assets")
	# copy res folder from SDK
	if os.path.exists(PythonLocation()+"/../../02_ChannelSdk/ChannelSDK/"+_ChannelName.lower()+"/res"):
		if os.path.exists(PythonLocation()+"/../../02_ChannelSdk/ChannelSDKSmali/"+_ChannelName+"/res"):
			DeleteFolder(PythonLocation()+"/../../02_ChannelSdk/ChannelSDKSmali/"+_ChannelName+"/res")
		CopyFiles(PythonLocation()+"/../../02_ChannelSdk/ChannelSDK/"+_ChannelName.lower()+"/res",PythonLocation()+"/../../02_ChannelSdk/ChannelSDKSmali/"+_ChannelName+"/res")
	if os.path.exists(PythonLocation()+"/__pycache__/"+SDKFolder+"/bin/app-release/smali"):
		if os.path.exists(PythonLocation()+"/../../02_ChannelSdk/ChannelSDKSmali/"+_ChannelName+"/smali"):
			DeleteFolder(PythonLocation()+"/../../02_ChannelSdk/ChannelSDKSmali/"+_ChannelName+"/smali")
		CopyFiles(PythonLocation()+"/__pycache__/"+SDKFolder+"/bin/app-release/smali",PythonLocation()+"/../../02_ChannelSdk/ChannelSDKSmali/"+_ChannelName+"/smali")
	if os.path.exists(PythonLocation()+"/__pycache__/"+SDKFolder+"/bin/app-release/lib"):
		if os.path.exists(PythonLocation()+"/../../02_ChannelSdk/ChannelSDKSmali/"+_ChannelName+"/lib"):
			DeleteFolder(PythonLocation()+"/../../02_ChannelSdk/ChannelSDKSmali/"+_ChannelName+"/lib")
		CopyFiles(PythonLocation()+"/__pycache__/"+SDKFolder+"/bin/app-release/lib",PythonLocation()+"/../../02_ChannelSdk/ChannelSDKSmali/"+_ChannelName+"/lib")
	os.chdir(r''+CallMethodPath)
def DecompileSDK(_ChannelName,De_APKName):
	SDKFolder = ""
	SDKFolder = CopyEmptyDemo(SDKFolder)
	CopySDKToFolder(_ChannelName,SDKFolder)
	DecompileSDKAPK(SDKFolder,_ChannelName)
	return SDKFolder
def CopyDecomplieAPK(_APKLocation):
	count = 1
	while True:
		if os.path.exists(PythonLocation()+"/__pycache__/de_copy"+str(count)+".apk"):
			count+=1
		else:
			break
	shutil.copy(_APKLocation,PythonLocation()+"/__pycache__/de_copy"+str(count)+".apk")
	return "de_copy"+str(count)+".apk"

@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def CheckAPKContainedSDK(_APKLocation):
	if CheckLen(_APKLocation) ==False:
		return
	De_APKName = CopyDecomplieAPK(_APKLocation)
	DecopileAPK(_APKLocation)
	DecompileSDK("east2west",De_APKName)
	
def CheckSignature(_APKLocation):
	Unzip(_APKLocation)
	SignatureCommond(_APKLocation)

def	ListFolder(path):
	List = []
	for i in os.listdir(path):
		List.append(i)
	return List

def DeleteFolder(src):
    '''delete files and folders'''
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc=os.path.join(src,item)
            DeleteFolder(itemsrc) 
        try:
            os.rmdir(src)
        except:
            pass



def CopyBaseAPK(_APKLocation):
	if os.path.isfile(PythonLocation()+"/__pycache__/copy.apk")==False:
		shutil.copy(_APKLocation,PythonLocation()+"/__pycache__/copy.apk")
	elif os.path.isfile(PythonLocation()+"/__pycache__/copy.apk"):
		os.remove(PythonLocation()+"/__pycache__/copy.apk")
		shutil.copy(_APKLocation,PythonLocation()+"/__pycache__/copy.apk")
	return PythonLocation()+"/__pycache__/copy.apk"
def CopyXMLToAPK(_APKLocation):
	os.chdir(r''+PythonLocation()+"/__pycache__")
	CopyThings = ""
	CopyThings += "AndroidManifest.xml"
	CopyThings += " "
	CopyThings += "resources.arsc"
	#print("jar uvf "+PythonLocation()+"/__pycache__/copy.apk "+CopyThings)
	os.system("jar uvf "+PythonLocation()+"/__pycache__/copy.apk "+CopyThings)
	os.chdir(r''+CallMethodPath)
def ResigneAPK(_APKLocation):
	DeleteSignature(PythonLocation()+"/__pycache__/copy.apk")
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	keyplace = PythonLocation()+"/../Appurtenance/grannysmith.keystore"
	signedAPKPlace = PythonLocation()+"/__pycache__/copy_signed.apk"
	resourceAPK = PythonLocation()+"/__pycache__/copy.apk"
	if os.path.isfile(PythonLocation()+"/copy_signed.apk"):
		os.remove(PythonLocation()+"/copy_signed.apk")
	#print(keyplace)
	#print(signedAPKPlace)
	#print(resourceAPK)
	#print("jarsigner -verbose -keystore " + keyplace +" -storepass hello123456 -signedjar " + signedAPKPlace + " -digestalg SHA1 -sigalg MD5withRSA " + resourceAPK + " android.keystore")
	os.system("jarsigner -verbose -keystore " + keyplace +" -storepass hello123456 -signedjar " + signedAPKPlace + " -digestalg SHA1 -sigalg MD5withRSA " + resourceAPK + " android.keystore")
	Location = MoveAPKToGameSDK(signedAPKPlace,foldername)
	return Location
def ResigneAPKOnly(_APKLocation):
	DeleteSignature(_APKLocation)
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	keyplace = PythonLocation()+"/../Appurtenance/grannysmith.keystore"
	signedAPKPlace = get_desktop()+"/GameAPK/"+foldername+"_signed.apk"
	resourceAPK = _APKLocation
	if os.path.isfile(PythonLocation()+"/copy_signed.apk"):
		os.remove(PythonLocation()+"/copy_signed.apk")
	#print(keyplace)
	#print(signedAPKPlace)
	#print(resourceAPK)
	#print("jarsigner -verbose -keystore " + keyplace +" -storepass hello123456 -signedjar " + signedAPKPlace + " -digestalg SHA1 -sigalg MD5withRSA " + resourceAPK + " android.keystore")
	os.system("jarsigner -verbose -keystore " + keyplace +" -storepass hello123456 -signedjar " + signedAPKPlace + " -digestalg SHA1 -sigalg MD5withRSA " + resourceAPK + " android.keystore")
	os.remove(_APKLocation)
	shutil.copy(signedAPKPlace,_APKLocation)
	#Location = MoveAPKToGameSDK(signedAPKPlace,foldername)
	Location = _APKLocation
	return Location
def MoveAPKToGameSDK(signedAPKPlace,foldername):
	i = 1
	while True:
		
		if os.path.isfile(get_desktop()+"/GameAPK/"+foldername+str(i)+".apk"):
			i+=1
			continue
		break
	#print("MoveAPKToGameSDK="+signedAPKPlace)
	os.rename(signedAPKPlace,get_desktop()+"/GameAPK/"+foldername+str(i)+".apk")
	return get_desktop()+"/GameAPK/"+foldername+str(i)+".apk"
def DeleteSignature(_APKLocation):
	#os.chdir(r''+"C:\MyProject\AgileTools")
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	# foldername=APKname[:PointCount]
	APKname[:PointCount]
	your_delet_file="META-INF"
	
	old_zipfile=_APKLocation #旧文件
	new_zipfile=_APKLocation+"temp" #新文件
	zin = zipfile.ZipFile (old_zipfile, 'r') #读取对象
	zout = zipfile.ZipFile (new_zipfile, 'w') #被写入对象
	for item in zin.infolist():
		buffer = zin.read(item.filename)
		if ((your_delet_file in item.filename) and (".RSA" in item.filename)) or ((your_delet_file in item.filename)and (".SF" in item.filename)) or ((your_delet_file in item.filename) and (".MF" in item.filename)):  #剔除要删除的文件
			pass
		else:
			zout.writestr(item, buffer) #把文件写入到新对象中
	zout.close()
	zin.close()
	print("Deleted Signature")
	#用新文件覆盖旧文件
	shutil.move(new_zipfile,old_zipfile)

def WriteE2WNumber(_APKLocation,_PackageName):
	_Path=_APKLocation
	dom = xml.dom.minidom.parse(_Path)
	root = dom.documentElement
	#name =root.getAttribute("package")
	name  = root.getElementsByTagName("meta-data")
	global FoundKey
	FoundKey=False
	for node in name:
		nameofname = node.getAttribute("android:name")
		if nameofname=="E2W_NUMBER":
			# nameofvalue = node.getAttribute("android:value")
			node.getAttribute("android:value")
			node.setAttribute("android:value",_PackageName)
			FoundKey=True
	if FoundKey==False:
		print("[ERROR] Can't find E2W_NUMBER")
	try:
		with open(_Path,'w',encoding='UTF-8') as _Path:
			dom.writexml(_Path,indent='',addindent='',newl='',encoding='UTF-8')
	except Exception as err:
		print("ERROR[{0}".format(err))
def ChangeChineseName(_APKLocation,_ChineseName):
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	_Path = PythonLocation()+"/__pycache__/"+foldername+"/AndroidManifest.xml"
	dom = xml.dom.minidom.parse(_Path)
	root = dom.documentElement
	#name =root.getAttribute("package")
	name  = root.getElementsByTagName("activity")
	for node in name:
		nameofname1 = node.getAttribute("android:label")
		nameofname2 = node.getAttribute("android:name")
		nameofname3 = node.getAttribute("android:screenOrientation")
		if nameofname1!="" and nameofname2!="" and nameofname3!="" :
			node.setAttribute("android:label",_ChineseName)
	name  = root.getElementsByTagName("application")
	for node in name:
		nameofname1 = node.getAttribute("android:name")
		nameofname2 = node.getAttribute("android:label")
		nameofname3 = node.getAttribute("android:icon")
		if nameofname1!="" and nameofname2!="" and nameofname3!="" :
			node.setAttribute("android:label",_ChineseName)
	try:
		with open(_Path,'w',encoding='UTF-8') as _Path:
			dom.writexml(_Path,indent='',addindent='',newl='',encoding='UTF-8')
	except Exception as err:
		print("ERROR[{0}".format(err))
def WriteoppoXML(_APKLocation,_PackageName):
	_Path=_APKLocation
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	#print(PythonLocation()+"/__pycache__/"+foldername+"/AndroidManifest.xml")
	_Path=PythonLocation()+"/__pycache__/"+foldername+"/AndroidManifest.xml"
	print(_Path+"   "+_PackageName)
	dom = xml.dom.minidom.parse(PythonLocation()+"/__pycache__/"+foldername+"/AndroidManifest.xml")
	root = dom.documentElement
	#name =root.getAttribute("package")
	name  = root.getElementsByTagName("meta-data")
	global FoundKey
	FoundKey=False
	for node in name:
		nameofname = node.getAttribute("android:name")
		if nameofname=="debug_mode":
			# nameofvalue = node.getAttribute("android:value")
			node.getAttribute("android:value")
			node.setAttribute("android:value",_PackageName)
			FoundKey=True
	if FoundKey==False:
		print("[ERROR] Can't find E2W_NUMBER")
	try:
		with open(_Path,'w',encoding='UTF-8') as _Path:
			dom.writexml(_Path,indent='',addindent='',newl='',encoding='UTF-8')
	except Exception as err:
		print("ERROR[{0}".format(err))

def ChangePackageVCVN(_APKLocation,VersionName,VersionCode):
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	_Path = PythonLocation()+"/__pycache__/"+foldername+"/apktool.yml"

	myfile = open(_Path,'rb')
	data = myfile.read()
	di= chardet.detect(data)
	myfile.close()

	if di["encoding"]=="UTF-8-SIG":
		file_object = open(_Path,'r',encoding="UTF-8-SIG")
		#print(di["encoding"])
	if di["encoding"]=="GB2312":
		file_object = open(_Path,'r',encoding="GB2312")
		#print(di["encoding"])
	if di["encoding"]=="utf-8":
		file_object = open(_Path,'r',encoding="utf-8")
	if di["encoding"]=="ascii":
		file_object = open(_Path,'r',encoding="ascii")
		#print(di["encoding"])
	JavaCode=[]
	try:
		all_the_text = file_object.readlines()
		for i in all_the_text:
			#print(i)
			if "versionCode" in i:
				#print("___VersionCode="+VersionCode)
				JavaCode.append("  versionCode: '"+VersionCode+"'\n")
			elif "versionName" in i:
				#print("___VersionName="+VersionName)
				JavaCode.append("  versionName: "+VersionName+"\n")
			else:
				JavaCode.append(i)
	finally:
		file_object.close( )
	
	if di["encoding"]=="UTF-8-SIG":
		file_object_read = open(_Path,'w',encoding="UTF-8-SIG")
		print(di["encoding"])
	if di["encoding"]=="GB2312":
		file_object_read = open(_Path,'w',encoding="GB2312")
		print(di["encoding"])
	if di["encoding"]=="utf-8":
		file_object_read = open(_Path,'w',encoding="utf-8")
		print(di["encoding"])
	if di["encoding"]=="ascii":
		file_object_read = open(_Path,'w',encoding="ascii")
		print(di["encoding"])
	#file_object_read = open(_Path,'w')
	try:
		#print(JavaCode)
		file_object_read.writelines(JavaCode)
	finally:
		file_object_read.close( )

@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def CheckAPKSignture(_APKLocation):
	_APKLocation = CheckLen(_APKLocation)
	Unzip(_APKLocation)
	SignatureCommond(_APKLocation)
	DecopileAPK(_APKLocation)
	print("-----------------------")
	print("  Package Name:  "+GetPackageName(_APKLocation)+"\n")
	List = GetVCVN(_APKLocation)
	print(List[0])
	print(List[1])
	print("  E2W_NUMBER(CPS):  "+GetPackageE2WNumber(_APKLocation)+"\n")
	print("  CHANNEL_NAME:  "+Get_METE(_APKLocation,"CHANNEL_NAME")+"\n")
	print("  EGAME_CHANNEL:  "+Get_METE(_APKLocation,"EGAME_CHANNEL")+"\n")
	print("  dksdk_ver:  "+Get_METE(_APKLocation,"dksdk_ver"))
	print("-----------------------")


@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def CheckAPKPackageName(_APKLocation,_PackageName):
	_APKLocation1= _APKLocation
	_APKLocation1 = _APKLocation1.replace("\\","/")
	APKname = _APKLocation1.split("/")[-1]
	PointCount = APKname.rfind(".")
	# foldername=APKname[:PointCount]
	APKname[:PointCount]
	_APKLocation = CheckLen(_APKLocation)
	APKname1 = _APKLocation.split("/")[-1]
	PointCount1 = APKname1.rfind(".")
	foldername1=APKname1[:PointCount1]
	DecopileAPK(_APKLocation)
	ChangePackageName(_APKLocation,_PackageName)
	RebuildAPK(PythonLocation()+"/__pycache__/"+foldername1)
	Unzip(PythonLocation()+"/__pycache__/"+foldername1+"/dist/"+foldername1+".apk")
	CopyBaseAPK(_APKLocation1)
	CopyXMLToAPK(_APKLocation1)
	ResigneAPK(_APKLocation1)
def METE_MODIFY(_Path,key, value):
	APKname = _Path.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	xmlLocation = PythonLocation()+"/__pycache__"+"/"+foldername+"/AndroidManifest.xml"
	dom = xml.dom.minidom.parse(xmlLocation)
	root = dom.documentElement
	#name =root.getAttribute("package")
	name  = root.getElementsByTagName("meta-data")
	global FoundKey
	FoundKey=False
	for node in name:
		nameofname = node.getAttribute("android:name")
		if nameofname==key:
			# nameofvalue = node.getAttribute("android:value")
			node.getAttribute("android:value")
			node.setAttribute("android:value",value)
			FoundKey=True
	if FoundKey==False:
		print("[ERROR] Can't find "+value)
	try:
		with open(xmlLocation,'w',encoding='UTF-8') as xmlLocation:
			dom.writexml(xmlLocation,indent='',addindent='',newl='',encoding='UTF-8')
	except Exception as err:
		print("ERROR[{0}".format(err))


@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def CheckAPKChannelName(_APKLocation,_ChannelName):
	_APKLocation1= _APKLocation
	_APKLocation1 = _APKLocation1.replace("\\","/")
	APKname1 = _APKLocation1.split("/")[-1]
	PointCount1 = APKname1.rfind(".")
	# foldername1=APKname1[:PointCount1]
	APKname1[:PointCount1]
	_APKLocation = CheckLen(_APKLocation)

	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	DecopileAPK(_APKLocation)
	METE_MODIFY(_APKLocation,"CHANNEL_NAME",_ChannelName)
	RebuildAPK(PythonLocation()+"/__pycache__/"+foldername)
	Unzip(PythonLocation()+"/__pycache__/"+foldername+"/dist/"+foldername+".apk")
	CopyBaseAPK(_APKLocation1)
	CopyXMLToAPK(_APKLocation)
	ResigneAPK(_APKLocation1)

@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def CheckAPKE2WNumber(_APKLocation,_PackageName):
	_APKLocation1= _APKLocation
	_APKLocation1 = _APKLocation1.replace("\\","/")
	APKname1 = _APKLocation1.split("/")[-1]
	PointCount1 = APKname1.rfind(".")
	foldername1=APKname1[:PointCount1]
	_APKLocation = CheckLen(_APKLocation)
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	DecopileAPK(_APKLocation)
	WriteE2WNumber(_APKLocation,_PackageName)
	RebuildAPK(PythonLocation()+"/__pycache__/"+foldername1)
	Unzip(PythonLocation()+"/__pycache__/"+foldername+"/dist/"+foldername+".apk")
	CopyBaseAPK(_APKLocation1)
	CopyXMLToAPK(_APKLocation)
	ResigneAPK(_APKLocation1)

@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def CheckAPKChineseName(_APKLocation,_PackageName):
	_APKLocation1= _APKLocation
	_APKLocation1 = _APKLocation1.replace("\\","/")
	APKname1 = _APKLocation1.split("/")[-1]
	PointCount1 = APKname1.rfind(".")
	# foldername1=APKname1[:PointCount1]
	APKname1[:PointCount1]
	_APKLocation = CheckLen(_APKLocation)
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	DecopileAPK(_APKLocation)
	ChangeChineseName(_APKLocation,_PackageName)
	RebuildAPK(PythonLocation()+"/__pycache__/"+foldername)
	Unzip(PythonLocation()+"/__pycache__/"+foldername+"/dist/"+foldername+".apk")
	CopyBaseAPK(_APKLocation1)
	CopyXMLToAPK(_APKLocation)
	ResigneAPK(_APKLocation1)

@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def CreateBaidu4APK(_APKLocation):
	channelList = ["13744","12999","14076","14146"]
	myfullname = _APKLocation
	for mychannelid in channelList:
		_APKLocation1= myfullname
		_APKLocation1 = _APKLocation1.replace("\\","/")
		APKname1 = _APKLocation1.split("/")[-1]
		PointCount1 = APKname1.rfind(".")
		foldername1=APKname1[:PointCount1]
		_APKLocation = CheckLen(_APKLocation)
		_APKLocation = _APKLocation.replace("\\","/")
		APKname = _APKLocation.split("/")[-1]
		PointCount = APKname.rfind(".")
		foldername=APKname[:PointCount]
		DecopileAPK(_APKLocation)
		METE_MODIFY(_APKLocation,"dksdk_channel",mychannelid)
		RebuildAPK(PythonLocation()+"/__pycache__/"+foldername)
		shutil.copy(PythonLocation()+"/__pycache__/"+foldername+"/dist/"+foldername+".apk",get_desktop()+"/GameAPK/"+foldername1+"_"+mychannelid+"_decomplie.apk")
		Postion = ResigneAPKOnly(get_desktop()+"/GameAPK/"+foldername1+"_"+mychannelid+"_decomplie.apk")

		if os.path.isfile(get_desktop()+"/GameAPK/"+foldername1+"_"+mychannelid+".apk"):
				os.remove(get_desktop()+"/GameAPK/"+foldername1+"_"+mychannelid+".apk")
		os.rename(Postion,get_desktop()+"/GameAPK/"+foldername1+"_"+mychannelid+".apk")

		Unzip(PythonLocation()+"/__pycache__/"+foldername+"/dist/"+foldername+".apk")
		CopyBaseAPK(_APKLocation1)
		CopyXMLToAPK(_APKLocation)
		Postion = ResigneAPK(_APKLocation)
		if os.path.isfile(get_desktop()+"/GameAPK/"+foldername1+"_"+mychannelid+".apk"):
				os.remove(get_desktop()+"/GameAPK/"+foldername1+"_"+mychannelid+".apk")
		os.rename(Postion,get_desktop()+"/GameAPK/"+foldername1+"_"+mychannelid+".apk")

@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def CreateOppo(_APKLocation):
	_APKLocation1= _APKLocation
	_APKLocation1 = _APKLocation1.replace("\\","/")
	APKname1 = _APKLocation1.split("/")[-1]
	PointCount1 = APKname1.rfind(".")
	foldername1=APKname1[:PointCount1]
	_APKLocation = CheckLen(_APKLocation)
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	DecopileAPK(_APKLocation)
	WriteoppoXML(_APKLocation,"true")
	RebuildAPK(PythonLocation()+"/__pycache__/"+foldername)
	Unzip(PythonLocation()+"/__pycache__/"+foldername+"/dist/"+foldername+".apk")
	CopyBaseAPK(_APKLocation1)
	CopyXMLToAPK(_APKLocation)
	Postion = ResigneAPK(_APKLocation)
	if os.path.isfile(get_desktop()+"/GameAPK/"+foldername1+"_true.apk"):
			os.remove(get_desktop()+"/GameAPK/"+foldername1+"_true.apk")
	os.rename(Postion,get_desktop()+"/GameAPK/"+foldername1+"_true.apk")
	CreateOppo_false(_APKLocation1)
	
def CreateOppo_false(_APKLocation):
	_APKLocation1= _APKLocation
	_APKLocation1 = _APKLocation1.replace("\\","/")
	APKname1 = _APKLocation1.split("/")[-1]
	PointCount1 = APKname1.rfind(".")
	foldername1=APKname1[:PointCount1]
	_APKLocation = CheckLen(_APKLocation)
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	DecopileAPK(_APKLocation)
	WriteoppoXML(_APKLocation,"false")
	RebuildAPK(PythonLocation()+"/__pycache__/"+foldername)
	Unzip(PythonLocation()+"/__pycache__/"+foldername+"/dist/"+foldername+".apk")
	CopyBaseAPK(_APKLocation1)
	CopyXMLToAPK(_APKLocation)
	Postion = ResigneAPK(_APKLocation)
	if os.path.isfile(get_desktop()+"/GameAPK/"+foldername1+"_false.apk"):
			os.remove(get_desktop()+"/GameAPK/"+foldername1+"_false.apk")
	os.rename(Postion,get_desktop()+"/GameAPK/"+foldername1+"_false.apk")
def CheckLen(_APKLocation):
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	i = 1
	while os.path.isfile(PythonLocation()+"/__pycache__/"+str(i)+".apk"):
		i=i+1
	shutil.copy(_APKLocation,PythonLocation()+"/__pycache__/"+str(i)+".apk")
	PointCount = APKname.rfind(".")
	# foldername=APKname[:PointCount]
	APKname[:PointCount]
	return PythonLocation()+"/__pycache__/"+ str(i)+".apk"
@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def CheckVCVN(_APKLocation,VersionName,VersionCode):
	_APKLocation1= _APKLocation
	_APKLocation1 = _APKLocation1.replace("\\","/")
	APKname1 = _APKLocation1.split("/")[-1]
	PointCount1 = APKname1.rfind(".")
	# foldername1=APKname1[:PointCount1]
	APKname1[:PointCount1]
	_APKLocation = CheckLen(_APKLocation)
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	DecopileAPK(_APKLocation)
	ChangePackageVCVN(_APKLocation,VersionName,VersionCode)
	RebuildAPK(PythonLocation()+"/__pycache__/"+foldername)
	Unzip(PythonLocation()+"/__pycache__/"+foldername+"/dist/"+foldername+".apk")
	CopyBaseAPK(_APKLocation1)
	CopyXMLToAPK(_APKLocation)
	# location  = ResigneAPK(_APKLocation1)
	ResigneAPK(_APKLocation1)

@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def Resgin(_APKLocation,_KeyPath):
	_APKLocation1= _APKLocation
	_APKLocation1 = _APKLocation1.replace("\\","/")
	APKname1 = _APKLocation1.split("/")[-1]
	FileLocation =_APKLocation1[:_APKLocation1.rfind("/")]
	PointCount1 = APKname1.rfind(".")
	foldername1=APKname1[:PointCount1]
	_APKLocation = CheckLen(_APKLocation)
	_APKLocationCopy = CopyBaseAPK(_APKLocation)
	DeleteSignature(_APKLocationCopy)
	_APKLocation = _APKLocation.replace("\\","/")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	keyplace = _KeyPath#PythonLocation()+"/../Appurtenance/grannysmith.keystore"
	signedAPKPlace = get_desktop()+"/"+foldername+".apk"
	resourceAPK = _APKLocationCopy
	count = 1
	while True:
		if os.path.isfile(get_desktop()+"/"+foldername+str(count)+".apk"):
			count+=1
		else:
			break
		signedAPKPlace = get_desktop()+"/"+foldername+str(count)+".apk"
	#print(keyplace)
	#print(signedAPKPlace)
	#print(resourceAPK)
	#print("jarsigner -verbose -keystore " + keyplace +" -storepass hello123456 -signedjar " + signedAPKPlace + " -digestalg SHA1 -sigalg MD5withRSA " + resourceAPK + " android.keystore")
	os.system("jarsigner -verbose -keystore " + keyplace +" -storepass hello123456 -signedjar " + signedAPKPlace + " -digestalg SHA1 -sigalg MD5withRSA " + resourceAPK + " android.keystore")
	count1 = 1
	while True:
		print(get_desktop()+"/GameAPK/"+foldername1+str(count1)+".apk")
		if os.path.isfile(get_desktop()+"/GameAPK/"+foldername1+str(count1)+".apk"):
			count1+=1
		else:
			break
	os.rename(signedAPKPlace,FileLocation+"/"+foldername1+str(count1)+".apk")
	return FileLocation+"/"+foldername1+str(count1)+".apk" 
def get_desktop():
	return os.path.join(os.path.expanduser("~"), 'Desktop')

def CopyFiles(sourceDir, targetDir):
    global copyFileCounts
    #print (sourceDir)
    #print (u"%s 当前处理文件夹%s已处理%s 个文件" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), sourceDir,copyFileCounts))
    for f in os.listdir(sourceDir):
        sourceF = os.path.join(sourceDir, f)
        targetF = os.path.join(targetDir, f)
        if os.path.isfile(sourceF):
            #创建目录
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            copyFileCounts += 1
            #文件不存在，或者存在但是大小不同，覆盖
            if not os.path.exists(targetF) or (os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
                #2进制文件
                open(targetF, "wb").write(open(sourceF, "rb").read())
                #print (u"%s %s 复制完毕" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), targetF))
            else:
                pass
                #print (u"%s %s 已存在，不重复复制" %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())), targetF))
        if os.path.isdir(sourceF):
            CopyFiles(sourceF, targetF)
@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def GetSmaliOfJar(_Location):
	#print("GetSmaliOfJar")
	if CheckLen(_Location) ==False:
		return
	if os.path.exists(PythonLocation()+"/../Appurtenance/DemoAPK"):
		if os.path.exists(PythonLocation()+"/__pycache__/DemoAPK"):
			DeleteFolder(PythonLocation()+"/__pycache__/DemoAPK")
		CopyFiles(PythonLocation()+"/../Appurtenance/DemoAPK",PythonLocation()+"/__pycache__/DemoAPK")
	if os.path.exists(PythonLocation()+"/__pycache__/DemoAPK/app/libs")==False:
		os.mkdir(PythonLocation()+"/__pycache__/DemoAPK/app/libs")
	shutil.copy(_Location,PythonLocation()+"/__pycache__/DemoAPK/app/libs/UnityPlugin.jar")
	os.chdir(PythonLocation()+"/__pycache__/DemoAPK")
	os.system(GetPythonCommand()+" BuildAPK.py")
	os.system(PythonLocation()+"/../Tool/apktool d "+PythonLocation()+"/__pycache__/DemoAPK/app-release.apk")
	if os.path.exists(PythonLocation()+"/__pycache__/DemoAPK/app-release/smali/test"):
		DeleteFolder(PythonLocation()+"/__pycache__/DemoAPK/app-release/smali/test")
	if os.path.exists(PythonLocation()+"/__pycache__/DemoAPK/app-release/smali/com/AmanitaDesign"):
		DeleteFolder(PythonLocation()+"/__pycache__/DemoAPK/app-release/smali/com/AmanitaDesign")
	if os.path.exists(PythonLocation()+"/../smali"):
		DeleteFolder(PythonLocation()+"/../smali")
	if os.path.exists(get_desktop()+"/smali"):
		DeleteFolder(get_desktop()+"/smali")
	CopyFiles(PythonLocation()+"/__pycache__/DemoAPK/app-release/smali",get_desktop()+"/smali")
	os.chdir(PythonLocation()+"/__pycache__")
	os.system(r"jar -xvf  "+PythonLocation()+"/__pycache__/DemoAPK/app/libs/UnityPlugin.jar")
	if os.path.exists(PythonLocation()+"/__pycache__/assets"):
		if os.path.exists(get_desktop()+"/assets"):
			DeleteFolder(get_desktop()+"/assets")
		CopyFiles(PythonLocation()+"/__pycache__/assets",get_desktop()+"/assets")
	print("Finished")
def GetEncoding(_Path):
	myfile = open(_Path,'rb')
	data = myfile.read()
	di= chardet.detect(data)
	myfile.close()
	myencoding = di["encoding"]
	return myencoding
def ChangeDemoPackageName(_Path,_PackageName):
    file_object = open(_Path,'r',encoding=GetEncoding(_Path))
    #print(di["encoding"])
    JavaCode=[]
    try:
        all_the_text = file_object.readlines()
        for i in all_the_text:
            if(i.find(".R")!=-1 and i.find("import")!=-1):
                JavaCode.append("import "+_PackageName+".R;\n")
            else:
                JavaCode.append(i)
    finally:
        file_object.close( )

    file_object_read = open(_Path,'w',encoding=GetEncoding(_Path))

    #file_object_read = open(_Path,'w')
    try:
        file_object_read.writelines(JavaCode)
    finally:
        file_object_read.close( )

@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def GetNULLPackage(_PackageName):
	if os.path.exists(PythonLocation()+"/../Appurtenance/DemoAPK"):
		if os.path.exists(PythonLocation()+"/__pycache__/DemoAPK"):
			DeleteFolder(PythonLocation()+"/__pycache__/DemoAPK")
		CopyFiles(PythonLocation()+"/../Appurtenance/DemoAPK",PythonLocation()+"/__pycache__/DemoAPK")
	SetGradlePackageName(PythonLocation()+"/__pycache__/DemoAPK/app/build.gradle",_PackageName)
	#ChangeDemoPackageName(PythonLocation()+"/__pycache__/DemoAPK/app/src/main/java/com/AmanitaDesign/testapp/MainActivity.java",_PackageName)
	os.chdir(PythonLocation()+"/__pycache__/DemoAPK")
	os.system("BuildAPK.bat")
	i = 0
	while True:
		i+=1
		if os.path.isfile(get_desktop()+"/GameAPK/"+_PackageName+str(i)+".apk"):
			continue
		break
	if os.path.isfile(PythonLocation()+"/__pycache__/DemoAPK/app-release.apk"):
		os.rename(PythonLocation()+"/__pycache__/DemoAPK/app-release.apk",get_desktop()+"/GameAPK/"+_PackageName+str(i)+".apk")
	else:
		print("Build Failed")

@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def DecompileAPKCall(_Path):
	_Path = _Path.replace("\\","/")
	APKname = _Path.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	_Path = CheckLen(_Path)
	_Path = _Path.replace("\\","/")
	APKname1 = _Path.split("/")[-1]
	PointCount1 = APKname1.rfind(".")
	foldername1=APKname1[:PointCount1]
	DecopileAPK(_Path)
	if os.path.exists(get_desktop()+"/"+foldername):
		DeleteFolder(get_desktop()+"/"+foldername)
	CopyFiles(PythonLocation()+"/__pycache__"+"/"+foldername1,get_desktop()+"/"+foldername)
@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def CompileAPKCall(_Path):
	_Path = _Path.replace("\\","/")
	APKname = _Path.split("/")[-1]
	PointCount = APKname.rfind(".")
	# foldername=APKname[:PointCount]
	APKname[:PointCount]
	RebuildAPK(_Path)
	List = ListFolder(_Path+"/dist")
	for f in List:
		if ".apk" in f:
			shutil.copy(_Path+"/dist/"+f,get_desktop()+"/GameAPK/"+APKname+".apk")
			location = Resgin(get_desktop()+"/GameAPK/"+APKname+".apk",)
			os.remove(get_desktop()+"/GameAPK/"+APKname+".apk")
			os.system("adb install -r "+location)

def  is_chinese(text):  
	hz_yes = False
	for  ch  in  text:
		if  isinstance(ch, str):
			if  unicodedata.east_asian_width(ch)!=  'Na' :  
				hz_yes = True
				break
		else :  
			continue
	return  hz_yes

def BingTranslateContext(key):
	key
	url = "https://cn.bing.com/ttranslationlookup?&IG=3EF2174489CC4319A90ECF75C534ABCB&IID=translator.5035.6"
	TranslateWord = key
	# isEnglish =key.isalpha()
	key.isalpha()
	is_chinese_b = is_chinese(key[0])
	if is_chinese_b==False:
		Myfrom = "en"
		Myto = "zh-CHS"
	else:
		Myfrom = "zh-CHS"
		Myto = "en"
	FormateData = {
	"text":TranslateWord,
	"from":Myfrom,
	"to":Myto
	}
	my_datas = urllib.parse.urlencode(FormateData).encode(encoding='UTF8')
	my_headers ={
		"Accept": "*/*",
		"Origin": "https://cn.bing.com",
		"Referer": "https://cn.bing.com/",
		"Accept-Language": "zh-Hans-CN,zh-Hans;q=0.7,ja;q=0.3",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
		"Content-type": "application/x-www-form-urlencoded",
		"Host": "cn.bing.com",
		"Connection": "Keep-Alive",
		"Cache-Control": "no-cache"
	}
	request  = urllib.request.Request (url,data = my_datas,headers = my_headers)
	text  = urllib.request.urlopen(request).read()

	url = "https://cn.bing.com/ttranslate?&category=&IG=3EF2174489CC4319A90ECF75C534ABCB&IID=translator.5035.8"
	TranslateWord = key
	FormateData = {
	"text":TranslateWord,
	"from":Myfrom,
	"to":Myto
	}
	my_datas = urllib.parse.urlencode(FormateData).encode(encoding='UTF8')
	my_headers ={
		"Accept": "*/*",
		"Origin": "https://cn.bing.com",
		"Referer": "https://cn.bing.com/",
		"Accept-Language": "zh-Hans-CN,zh-Hans;q=0.7,ja;q=0.3",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
		"Content-type": "application/x-www-form-urlencoded",
		"Host": "cn.bing.com",
		"Connection": "Keep-Alive",
		"Cache-Control": "no-cache"
	}
	request  = urllib.request.Request (url,data = my_datas,headers = my_headers)
	text  = urllib.request.urlopen(request).read()

	#print(text)
	#print(text.decode("UTF-8"))
	target = json.loads(text.decode("UTF-8"))
	results = target['translationResponse']
	return results

def FindTranslateWords_BitHero(_Location,Filename):
	#print(sys.path[0]+"/01_E2WSDKPlugin/src/com/east2west/game/SdkApplication.java")
	if os.path.isfile(_Location+Filename):
		file_object = open(_Location+Filename,encoding=GetEncoding(_Location+Filename))
		JavaCode=[]
		try:
			all_the_text = file_object.readlines()
			for i in all_the_text:
				if(i.find("<string lang=\"en\">")!=-1):
					StartString = i.find("<string lang=\"en\">")
					EndString = i.find("</string>")
					TranslateString  = i[StartString+len("<string lang=\"en\">"):EndString]
					print("[Translating]"+TranslateString+".....")
					Twords = BingTranslateContext(TranslateString)
					newString  = "		<string lang=\"zh\">"+Twords+"</string>\n"
					print("[Translated]"+Twords+".....")
					JavaCode.append(newString)
					JavaCode.append(i)
				else:
					JavaCode.append(i)
		finally:
			file_object.close( )
		
		file_object_read = open(_Location+"Translated/"+Filename+"_",'w',encoding=GetEncoding(_Location+"/Translated/"+Filename+"_"))
		try:
			file_object_read.writelines(JavaCode)
		finally:
			file_object_read.close( )
		if os.path.exists(_Location+"Translated/"+Filename):
			os.remove(_Location+"Translated/"+Filename)
		os.rename(_Location+"Translated/"+Filename+"_",_Location+"Translated/"+Filename)

@CallMethodLocation("")
@UsePlatform("Windows")
@RegistDragPromission("DragPromission")
def Translate(_Path):
	_Path = _Path.replace("\\","/")
	APKname = _Path.split("/")[-1]
	foldername=APKname
	LocationNumber =  _Path.rfind("/")
	Location = _Path[:LocationNumber]

	Mylist = ListFolder(Location+"/"+foldername)
	for ReadList in Mylist:
		if(ReadList.find(".")==-1):
			continue
		if(os.path.exists(Location+"/"+foldername+"/Translated/"+ReadList)==True):
			print("Skip:"+ReadList)
			continue
		if os.path.exists(Location+"/"+foldername+"/Translated")==False:
			os.mkdir(Location+"/"+foldername+"/Translated")
		shutil.copy(Location+"/"+foldername+"/"+ReadList, Location+"/"+foldername+"/Translated/"+ReadList+"_")
		FindTranslateWords_BitHero(Location+"/"+foldername+"/",ReadList)
def get_chinese_names(folder_dict: dict) -> [str]:
	list = []
	for name in folder_dict.values():
		if len(name) > 1:
			list.append(name[1])
		else:
			list.append("")
	return list
def get_english_names(folder_dict: dict) -> [str]:
	return [name[0] for name in folder_dict.values()]
def get_key_names(folder_dict: dict) -> [str]:
	list = []
	for name in folder_dict.keys():
		if len(name) > 1:
			list.append(name)
		else:
			list.append("")
	return list
def get_game_names(filename: str) -> [str]:
	d = json.load(open(filename, encoding = 'utf-8'))
	return get_english_names(d) + get_chinese_names(d)+ get_key_names(d)
def CreateAllSignatrure():
	if os.path.exists(PythonLocation()+"/../Keystore")==False:
		os.mkdir(PythonLocation()+"/../Keystore")
	os.chdir(PythonLocation()+"/../Keystore")
	if os.path.isfile(PythonLocation()+"/../"+"folder.json")==False:
		print(PythonLocation()+"/../"+"folder.json is not exist" )
	key = get_key_names(json.load(open(PythonLocation()+"/../"+"folder.json", encoding = 'utf-8')))
	games = get_english_names(json.load(open(PythonLocation()+"/../"+"folder.json", encoding = 'utf-8')))
	games_cn = get_chinese_names(json.load(open(PythonLocation()+"/../"+"folder.json", encoding = 'utf-8')))
	count= 0
	for i in games:
		Signature(key[count],i,games_cn[count])
		count+=1
def Signature(_key,_name,_gamename):
	_key = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",_key)
	_key = _key.replace(" ","")
	_name = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",_name)
	_name = _name.replace(" ","")
	_gamename = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "",_gamename)
	_gamename = _gamename.replace(" ","")
	list = ListFolder(PythonLocation()+"/../Keystore")
	for my in list:
		if(my.find(_key)!=-1):
			print("Already Create Game:"+_key)
			return 
	#p = Popen(["python3", "/Users/yupengqin/MyPragram/E2WGAME/03_Appurtenance/031_双击打空包.py"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
	os.system("keytool -genkey -alias android.keystore \
    -keyalg RSA -keystore "+_key+"_"+_name+"_"+_gamename+".keystore \
    -dname \"CN="+_key+", OU="+_gamename+", O="+_name+", L=东品游戏, S=east2west, C=中国\" \
    -storepass hello123456 -keypass hello123456")
	#os.system("echo hello123456  | keytool -genkey -alias "+_name+".keystore -keyalg RSA -validity 20000 -keystore "+_name+".keystore")
def main():
	#DeleteSignature("C:/MyProject/AgileTools/abc.apk")
	
	#Signature("grannysmith")
	CreateAllSignatrure()
if __name__ == '__main__':
	main()