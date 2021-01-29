# import cv2  
# import numpy
import os
from PIL import Image, ImageDraw, ImageFont
import sys
#pip3 install opencv-python
#pip3 install numpy
def GetFilePathInfo(_path):
	postionMac = _path.rfind("/")
	postionWindows = _path.rfind("\\")
	String = []
	if postionMac!=-1:
		Path = _path[:postionMac]
		FileName = _path[postionMac+1:]
		symble = "/"
		FileNameShort = FileName[:FileName.rfind(".")]
	elif postionWindows!=-1:
		Path = _path[:postionWindows]
		FileName = _path[postionWindows+1:]
		symble = "\\"
		FileNameShort = FileName[:FileName.rfind(".")]
	String.append(Path)
	String.append(symble)
	String.append(FileName)
	String.append(FileNameShort)
	return String

def PythonLocation():
	return os.path.dirname(os.path.realpath(__file__))

# def CombinePicOpenVC(_pathPic1,_pathPic2):
# 	img1 = cv2.imread(ModifySizeOfPicTo512(_pathPic1),cv2.IMREAD_COLOR)
# 	img2 = cv2.imread(ModifySizeOfPicTo512(_pathPic2),cv2.IMREAD_COLOR)
# 	myRect = img1[280:340, 330:390]
# 	img2.copyTo(myRect)
# 	cv2.imshow("1",img1)
# 	img_mix = cv2.addWeighted(img1, 1, img2,1, 0,)
# 	cv2.imwrite(GetFilePathInfo(_pathPic1)[0]+GetFilePathInfo(_pathPic1)[1]+"app_icon_"+GetFilePathInfo(_pathPic2)[3]+".png", img_mix)
# 	aaa = cv2.imread(GetFilePathInfo(_pathPic1)[0]+GetFilePathInfo(_pathPic1)[1]+"app_icon_"+GetFilePathInfo(_pathPic2)[3]+".png")
# 	cv2.imshow("2",aaa)
# 	cv2.waitKey(0)
def ModifySizeOfPicTo512(_PicLocation):
	pic = Image.open(_PicLocation)
	pic = pic.resize((512, 512))
	pic.save(_PicLocation)
	return _PicLocation
def	ListFolder(path):
	List = []
	for i in os.listdir(path):
		List.append(i)
	return List
def add_num(im,mark):
	background= im
	foreground= mark
	final2 = Image.new("RGBA", background.size)
	final2 = Image.alpha_composite(final2, background)
	final2 = Image.alpha_composite(final2, foreground)
	nameList = GetFilePathInfo(mark.filename)
	if os.path.isfile(nameList[0]+nameList[1]+"/../app_icon_"+nameList[3]+".png"):
		os.remove(nameList[0]+nameList[1]+"/../app_icon_"+nameList[3]+".png")
	final2.save(nameList[0]+nameList[1]+"/../app_icon_"+nameList[3]+".png")
	print("->New Icon:"+nameList[0]+nameList[1]+"/../app_icon_"+nameList[3]+".png")
def main(_ICONLocation):
	ListAllIcon = ListFolder(PythonLocation()+"/"+"ChannelIcon")
	for iconPlace in ListAllIcon:
		if iconPlace.rfind(".png")!=-1 and _ICONLocation.rfind(".png")!=-1:
			#CombinePicOpenVC(PythonLocation()+"/"+gameicon,PythonLocation()+"/"+"ChannelIcon/"+iconPlace)
			add_num(Image.open(ModifySizeOfPicTo512(_ICONLocation)),Image.open(ModifySizeOfPicTo512(PythonLocation()+"/"+"ChannelIcon/"+iconPlace)))
if __name__=='__main__':
	print("[Your Icon:"+PythonLocation()+"/"+sys.argv[1]+"]")
	main(sys.argv[1])
	print("Press any keys to exit...")
	input()