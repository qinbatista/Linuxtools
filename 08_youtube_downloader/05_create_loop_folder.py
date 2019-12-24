import sys, os, platform,time,shutil

def main():
	f_list = os.listdir("/root/ShareFolder/YoutubeDownlaod/")
	print(str(f_list))
	print(str(os.path.abspath(__file__)))
	dirname,filename=os.path.split(os.path.abspath(__file__))
	for list in f_list:
		if os.path.isdir("/root/ShareFolder/YoutubeDownlaod/"+list):
			if os.path.exists("/root/ShareFolder/YoutubeDownlaod/"+list+"/03_loop_download_list.py"):
				os.system("rm "+"/root/ShareFolder/YoutubeDownlaod/"+list+"/03_loop_download_list.py")
			shutil.copy(dirname+"/03_loop_download_list.py","/root/ShareFolder/YoutubeDownlaod/"+list+"/03_loop_download_list.py")
if __name__ == '__main__':
    main()

#PLCJcQMZOafIAfS9sz0L9VSqKN0Cmr0E-1 #linux
#PLhXu26RzZZTwus4cNbPTcgXXH6oavT6EB#ai
#PL2DywIam67jsFoEhIvVhB0HukSP8IAIt0#wenzhao
#PLYtoePJQbGmhmTi5p5yklGaX5vakayZbf#粒子故事会
#PLYtoePJQbGmicW5EiJeVIgz5a4Br99WwC#天文史记
#PLkz_-SLZY0iD4u99bFkSE_jQ_VXXbirLb#幻海航行
#PLqgfngs2pxpRTLCipUSnaQaf3qlST8d-8#音乐列表
