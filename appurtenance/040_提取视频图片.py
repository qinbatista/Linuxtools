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
def	ListFolder(path):
	List = []
	for i in os.listdir(path):
		List.append(i)
		breakw
	return List
def main():
	#_Path = sys.argv[1]
	#_Path = r"C:\Users\qinba\Desktop\GoldenGoalSoccer_Base_baidu_N1.3.7_C52310_2018_05_18_15_00_27.apk"
	print("Input your video location:")
	videoLocation = input()
	mypath = os.path.dirname(videoLocation)
	mybase = os.path.basename(videoLocation)
#	os.system("ffmpeg -i /Users/yupengqin/Desktop/sd1551072138_2.MP4  -r 10 -f image2 /Users/yupengqin/Desktop/Video/%05d.png")
	if os.path.isfile(videoLocation+"/VideoToPicture.mp3"):
		os.remove(videoLocation+"/VideoToPicture.mp3")
	#10一秒10帧 png可以切换的图片格式
	os.system("ffmpeg -i "+videoLocation+" -f mp3 -vn "+mypath+"/VideoToPicture.mp3")
	#os.system("ffmpeg -threads 2 -f image2 -i "+videoLocation+"/%0"+str(fileLen)+"d.png -vcodec libx264 -r 60 "+videoLocation+"/VideoToPicture.mp4")
if __name__ == '__main__':
    main()