import sys, os, platform
def get_desktop():
	return os.path.join(os.path.expanduser("~"), 'Desktop')
def main():
	# pip3 install youtube-dl
	print("Input List Number:")
	MyPackageName = input()
	os.system("youtube-dl -cit  --no-check-certificate https://www.youtube.com/playlist\?list\="+ MyPackageName)
if __name__ == '__main__':
    main()

#PLCJcQMZOafIAfS9sz0L9VSqKN0Cmr0E-1 #linux
#PLhXu26RzZZTwus4cNbPTcgXXH6oavT6EB#ai
#PL2DywIam67jsFoEhIvVhB0HukSP8IAIt0#wenzhao
#PLYtoePJQbGmhmTi5p5yklGaX5vakayZbf#粒子故事会
#PLYtoePJQbGmicW5EiJeVIgz5a4Br99WwC#天文史记
#PLkz_-SLZY0iD4u99bFkSE_jQ_VXXbirLb#幻海航行
#PLqgfngs2pxpRTLCipUSnaQaf3qlST8d-8#音乐
#PLqgfngs2pxpTAZlAt7Erjf8v97N_3T9FA#download_list
