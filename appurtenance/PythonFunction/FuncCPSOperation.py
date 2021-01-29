import sys, os, platform
import os
import time
import shutil
import chardet
import sys,os
import xml.dom.minidom
import zipfile
FoundKey = False
def UsePlatform():
	sysstr = platform.system()
	if(sysstr =="Windows"):
		return "Windows"
	elif(sysstr == "Linux"):
		return "Linux"
	else:
		return "Mac"
def PythonLocation():
	return os.path.dirname(os.path.realpath(__file__))
def CheckLen(_APKLocation):
	APKname = _APKLocation.split("/")[-1]
	i = 1
	while os.path.isfile(PythonLocation()+"/__pycache__/"+str(i)+".apk"):
		i=i+1
	shutil.copy(_APKLocation,PythonLocation()+"/__pycache__/"+str(i)+".apk")
	PointCount = APKname.rfind(".")
	# foldername=APKname[:PointCount]
	APKname[:PointCount]
	return str(i)+".apk"
def CreateCPS(Number,Location,key):
	for i in range(int(Number)):
		#Location = CheckLen(Location)
		if UsePlatform()=="Windows":
			RegistDragPromission()
		if os.path.exists(get_desktop()+"/GameAPK")==False:
			os.mkdir(get_desktop()+"/GameAPK")
		BuildAPK(str(i+1),Location,key)

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
	os.chdir(r''+"../")
	os.chdir(r''+"../")
def DeleteSignature(_APKLocation):
	#os.chdir(r''+"C:\MyProject\AgileTools")
	APKname = _APKLocation.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
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

def BuildAPK(Number,Location,key):
	#print(Number)
	print("Starting "+"east2west"+Number)
	os.chdir(PythonLocation()+"/__pycache__")
	global FoundKey
	DeleteSignature(Location)
	APKname = Location.split("/")[-1]
	PointCount = APKname.rfind(".")
	foldername=APKname[:PointCount]
	#print(foldername)
	#checkSign
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
	print("jar xf "+Location)
	os.system("jar xf "+Location)
	if os.path.exists(os.path.abspath('.')+"/META-INF"):
		print("[Python Notice] Please delete android signature and try again(delete /META-INF folder)")
		return
	#decompileAPK
		
	if os.path.exists(os.path.abspath('.')+"/"+foldername):
		DeleteFolder(os.path.abspath('.')+"/"+foldername)
	os.system(os.path.abspath('.')+"/../../Tool/apktool d "+Location)


	#modifyXML
	ChangeXML(os.path.abspath('.')+"/../../PythonFunction/__pycache__/"+foldername+"/AndroidManifest.xml","east2west"+Number)
	if(FoundKey == False):
		return
	#rebuildAPK
	os.system(os.path.abspath('.')+"/../../Tool/apktool b "+os.path.abspath('.')+"/../../PythonFunction/__pycache__/"+foldername)
	#unzipAPK
	if os.path.exists(os.path.abspath('.')+"/assets"):
		DeleteFolder(os.path.abspath('.')+"/assets")
	if os.path.exists(os.path.abspath('.')+"/META-INF"):
		DeleteFolder(os.path.abspath('.')+"/META-INF")
	if os.path.exists(os.path.abspath('.')+"/res"):
		DeleteFolder(os.path.abspath('.')+"/res")
	if os.path.isfile(os.path.abspath('.')+"/AndroidManifest.xml"):
		os.remove(os.path.abspath('.')+"/AndroidManifest.xml")
	if os.path.isfile(os.path.abspath('.')+"/classes.dex"):
		os.remove(os.path.abspath('.')+"/classes.dex")
	if os.path.isfile(os.path.abspath('.')+"/resources.arsc"):
		os.remove(os.path.abspath('.')+"/resources.arsc")
	os.system("jar xf "+os.path.abspath('.')+"/../../PythonFunction/__pycache__/"+foldername+"/dist/"+foldername+".apk")
	#copy APK to build
	#print(os.path.abspath('.')+"/../../PythonFunction\__pycache__/copy.apk")
	if os.path.isfile(os.path.abspath('.')+"/../../PythonFunction/__pycache__/copy.apk")==False:
		shutil.copy(Location,os.path.abspath('.')+"/../../PythonFunction/__pycache__/copy.apk")
		#print(os.path.abspath('.')+"/../../PythonFunction\__pycache__/copy.apk")
	#input()
	#copy xml to the APK
	CopyThings = ""
	CopyThings+="AndroidManifest.xml"
	CopyThings+= " "
	CopyThings+="resources.arsc"
	#print("jar uvf "+os.path.abspath('.')+"/../../PythonFunction\__pycache__/copy.apk "+CopyThings)
	os.system("jar uvf "+os.path.abspath('.')+"/../../PythonFunction/__pycache__/copy.apk "+CopyThings)
	#resignAPK
	#input()
	keyplace = key #os.path.abspath('.')+"/../../Appurtenance/grannysmith.keystore"
	signedAPKPlace = os.path.abspath('.')+"/../../PythonFunction/__pycache__/copy_signed.apk"
	resourceAPK = os.path.abspath('.')+"/../../PythonFunction/__pycache__/copy.apk"
	if os.path.isfile(os.path.abspath('.')+"/copy_signed.apk"):
		os.remove(os.path.abspath('.')+"/copy_signed.apk")
	print("jarsigner -verbose -keystore " + keyplace +"-storepass hello123456 -signedjar " + signedAPKPlace + " -digestalg SHA1 -sigalg MD5withRSA " + resourceAPK + " android.keystore")
	os.system("jarsigner -verbose -keystore " + keyplace+" -storepass hello123456 -signedjar " + os.path.abspath('.')+"/../../PythonFunction/__pycache__/copy_signed.apk" + " -digestalg SHA1 -sigalg MD5withRSA " + os.path.abspath('.')+"/../../PythonFunction/__pycache__/copy.apk" + " android.keystore")
	if os.path.isfile(get_desktop()+"/GameAPK/"+foldername+"_"+Number+".apk"):
		os.remove(get_desktop()+"/GameAPK/"+foldername+"_"+Number+".apk")
	os.rename(signedAPKPlace,get_desktop()+"/GameAPK/"+foldername+"_"+Number+".apk")
	os.chdir(r''+"../")
	os.chdir(r''+"../")
	print("Finished "+"east2west"+Number)
def get_desktop():
	return os.path.join(os.path.expanduser("~"), 'Desktop')
	
def ChangeXML(_Path,_PackageName):
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
# def CompareKeyWord(KeyWord,Location):
# 	DataList = GetData()
# 	MyDataList = GetMyData(Location)
# 	CountLine= 0
# 	if(KeyWord=="Chinese"):
# 		for i in MyDataList:
# 			for j in DataList:
# 				if j in i:
# 					if(i!="\n" and j!="\n" and i!="" and j!="" and i!= None and j!= None):
# 						print("Line ["+str(CountLine)+"] found sensitive context:"+j+"->your context:"+i)
# 						break
# 			CountLine+=1
# 	if(KeyWord=="English"):
# 		DataList1=[chr(i) for i in range(97,123)]
# 		DataList2=[chr(i) for i in range(65,91)]
# 		for my in DataList2:
# 			DataList1.append(my)
# 		#print(DataList1)
# 		for i in MyDataList:
# 			for j in DataList1:
# 				if j in i:
# 					#if(i!="\n" and j!="\n" and i!="" and j!="" and i!= None and j!= None):
# 					print("Line ["+str(CountLine)+"] found sensitive context:"+j+"->your context:"+i)
# 					break
# 			CountLine+=1
def main():
	#ChangeDemoPackageName(os.path.abspath('.')+"/../DemoProject/"+"02_ChannelDemo"+"Copy"+"/src/com/east2west/testapp/MainActivity.java",ReadXml_GetPackageName(os.path.abspath('.')+"/../DemoProject/"+"02_ChannelDemo"+"Copy"+"/AndroidManifest.xml"))
	#input()
	#print(ReadXml_GetPackageName(os.path.abspath('.')+"/../DemoProject/"+"02_ChannelDemo"+"Copy"+"/AndroidManifest.xml"))
	pass
if __name__ == '__main__':
    main()