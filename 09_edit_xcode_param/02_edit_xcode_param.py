import sys, os
import platform
from pbxproj import XcodeProject
from pbxproj.pbxextensions.ProjectFiles import FileOptions
import json
def get_desktop():
	return os.path.join(os.path.expanduser("~"), 'Desktop')
def PythonLocation():
	return os.path.dirname(os.path.realpath(__file__))
def CurrentPlatform():
	sysstr = platform.system()
	if(sysstr =="Windows"):
		return "Windows"
	elif(sysstr == "Linux"):
		return "Linux"
	elif(sysstr == "Darwin"):
		return "Mac"
	else:
		return "None"
def FindIOSSDKSource(_path):
	ListMyFolder = []
	for dirpath, dirnames, filenames in os.walk(_path):
		#print ('Directory', dirpath)
		dirnames
		for filename in filenames:
			#print (' File', filename)
			AllPath = dirpath+"/"+filename
			if AllPath.find(".DS_Store")==-1 and AllPath.find(".bundle/")==-1 and AllPath.find(".framework/")==-1:
				ListMyFolder.append(dirpath+"/"+filename)
			else:
				if  AllPath.find(".DS_Store")==-1:
					if AllPath.find(".framework/")!=-1:
						package = AllPath[:AllPath.find(".framework/")+len(".framework/")-1]
						if ListMyFolder.count(package)<=0:
							ListMyFolder.append(package)
					elif AllPath.find(".bundle/")!=-1:
						package = AllPath[:AllPath.find(".bundle/")+len(".bundle/")-1]
						if ListMyFolder.count(package)<=0:
							ListMyFolder.append(package)
					else:
						ListMyFolder.append(package)
	return ListMyFolder
def AddIOSSDK(_XcodeProjLocation,_SDKLocation):
	MyList = FindIOSSDKSource(_SDKLocation)
	project = XcodeProject.load(_XcodeProjLocation)
	for i in MyList:
		if i.find(".framework")!=-1:
			frameworks = project.get_or_create_group('Frameworks')
			# project.add_file(i, parent=frameworks,tree='SDKROOT', force=False, file_options=file_options)
			file_options = FileOptions(weak=True)
			project.add_file(i, parent=frameworks, force=False, file_options=file_options)
		else:
		 	project.add_file(i, force=False,file_options=FileOptions(weak=True,create_build_files=True))
	project.save()
def ReplaceKeyWord(_Path,keyword,nextLine):
	if os.path.isfile(_Path):
		file_object = open(_Path,encoding="utf8")
	JavaCode=[]
	isJump=False
	try:
		all_the_text = file_object.readlines()
		for i in all_the_text:
			if(i.find(keyword)!=-1):
				JavaCode.append(i)
				if CurrentPlatform()=="Windows":
					JavaCode.append(nextLine+"\n")
				if CurrentPlatform()=="Mac":
					JavaCode.append(nextLine+"\r")
				isJump=True
			else:
				if isJump:
					isJump=False
				else:
					JavaCode.append(i)
	finally:
		file_object.close( )

	file_object_read = open(_Path,'w',encoding="utf8")
	try:
		file_object_read.writelines(JavaCode)
	finally:
		file_object_read.close()
def AddIOSFlag(_XcodeProjLocation,_configuration):
	project = XcodeProject.load(_XcodeProjLocation)
	project.add_other_ldflags(_configuration)
	project.save()
def AddIOSLibrary(_XcodeProjLocation,_LibraryName):
	project = XcodeProject.load(_XcodeProjLocation)
	frameworks = project.get_or_create_group('Frameworks')
	file_options = FileOptions(weak=True)
	for i in _LibraryName:
		path = "/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk/System/Library/Frameworks/"+i+".framework"
		if os.path.exists(path):
			project.add_file(path, parent=frameworks, force=False, file_options=file_options)
		else:
			print("Can't find "+path)
	project.save()
def ChangeSetting(PbxprojPath,KetWord,replaceLine):
	ReplaceKeyWord(PbxprojPath,KetWord,replaceLine)
def main():
	_IOSPath=""#your xcode folder location
	_AD = ""#your sdk folder
	#pip3 install pbxproj
	PbxprojPath= _IOSPath+"/Unity-iPhone.xcodeproj/project.pbxproj"
	#add iossdk
	AddIOSSDK(PbxprojPath,PythonLocation()+"/../../02_ChannelSdk/ADIOSSDK/"+_AD) 
	#add library
	readed = json.load(open(PythonLocation()+"/../../02_ChannelSdk/ADIOSXML/"+_AD+"/Setting.json", 'r',encoding="UTF-8"))
	LibraryList = []
	FlagList = []
	for i in readed["library"]:
		LibraryList.append(i)
	for i in readed["flag"]:
		FlagList.append(i)
	AddIOSLibrary(PbxprojPath,LibraryList)
	#add flag
	AddIOSFlag(PbxprojPath,FlagList)
	#common setting
	ChangeSetting(PbxprojPath,"name = \"Embed Frameworks\";","			runOnlyForDeploymentPostprocessing = 1;")

if __name__ == '__main__':
    main()