import sys, os, platform,time
import subprocess
def main():
	# pip3 install youtube-dl
	MyPackageName=""
	while MyPackageName=="":
		print("Input List Number:")
		MyPackageName = input()
	while True:
		os.system(r"youtube-dl -o '%(playlist_index)s. %(title)s.%(ext)s'  --all-subs --no-check-certificate "+ MyPackageName)
		print("download again")
		time.sleep(2)
if __name__ == '__main__':
    main()



#国家地理
#https://www.youtube.com/user/NationalGeographic/playlists

#我的同步列表
#https://www.youtube.com/playlist?list=PLqgfngs2pxpTAZlAt7Erjf8v97N_3T9FA

#妈咪说
#https://www.youtube.com/channel/UCLROLAN8kmU7tGQDs6KH-bQ/playlists

#Linux教学
#https://www.youtube.com/playlist?list=PLCJcQMZOafIAfS9sz0L9VSqKN0Cmr0E-1

#幻海航行
#https://www.youtube.com/channel/UCp1nO1bgVwks9b5EhKQGVag/playlists

#文昭谈古论今
#https://www.youtube.com/channel/UCtAIPjABiQD3qjlEl1T5VpA/playlists

#人工智能教学
#https://www.youtube.com/playlist?list=PLhXu26RzZZTwus4cNbPTcgXXH6oavT6EB

#音乐列表
#https://www.youtube.com/playlist\?list\=PLqgfngs2pxpRTLCipUSnaQaf3qlST8d-8




