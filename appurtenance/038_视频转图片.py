import sys, os, platform
import shutil
def get_desktop():
	return os.path.join(os.path.expanduser("~"), 'Desktop')
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
def main():
	#_Path = sys.argv[1]
	#_Path = r"C:\Users\qinba\Desktop\GoldenGoalSoccer_Base_baidu_N1.3.7_C52310_2018_05_18_15_00_27.apk"
	print("Input your video location:")
	videoLocation = input()
	mypath = os.path.dirname(videoLocation)
	mybase = os.path.basename(videoLocation)
#	os.system("ffmpeg -i /Users/yupengqin/Desktop/sd1551072138_2.MP4  -r 10 -f image2 /Users/yupengqin/Desktop/Video/%05d.png")
	if os.path.exists(mypath+"/VideoToPicture")==False:
		os.mkdir(mypath+"/VideoToPicture")
	else:
		DeleteFolder(mypath+"/VideoToPicture")
		os.mkdir(mypath+"/VideoToPicture")
	#10一秒10帧 png可以切换的图片格式
	os.system("ffmpeg -i  "+videoLocation+" -r 60 -f image2 "+mypath+"/VideoToPicture/%05d.png")
if __name__ == '__main__':
    main()