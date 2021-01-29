# -*- coding: utf-8 -*- 
import urllib.request
import random
import json
import xml.dom.minidom
import unicodedata
import os
UA_List_PC =[
		"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
	  "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
	  "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
	  "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
	  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
	  "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
	  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	  "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	  "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
	  "User-Agent:Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
	  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
	  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
	  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
	  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
	  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
		]
UA_List_Mobile = [
		"Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
		"MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
		"JUC (Linux; U; 2.3.7; zh-cn; MB200; 320*480) UCWEB7.9.3.103/139/999",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1 Fennec/7.0a1",
		"Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
		"Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
		"Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/1A542a Safari/419.3",
		"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7",
		"Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
		"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A403 Safari/8536.25",
		"Mozilla/5.0 (iPad; CPU OS 5_0_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A405 Safari/7534.48.3",
		]
def	ListFolder(path):
	List = []
	for i in os.listdir(path):
		List.append(i)
	return List

def urlrequest(): 
	wd  = {"q":"覃于澎"}
	print("http://www.bing.com/search?"+urllib.parse.urlencode(wd))
	html= ReadPage("http://www.bing.com/search?"+urllib.parse.urlencode(wd))
	WritePage(html,"abc")
def ReadPage(url):
	UseAgent = random.choice(UA_List_PC)
	my_headers = {"User-Agent":UseAgent}
	request  = urllib.request.Request (url,headers = my_headers)
	print("正在读取网页")
	html = urllib.request.urlopen(request).read()
	print("读取网页完毕")
	#print(html.decode('utf-8'))
	return html
def WritePage(html,filename):
	print("正在下载网页")
	with open(filename, "wb+") as f:
		f.write(html)
	print("下载网页完毕")
def YoudaoTranslate(key):
	url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
	TranslateWord = key
	FormateData = {
	"i":TranslateWord,
	"from":"zh-CHS",
	"to":"to=en",
	"smartresult":"dict",
	"client":"fanyideskweb",
	"salt":"1525787891750",
	"sign":"2d8c81cf37929314d1bd5cd13a87c79c",
	"doctype":"json",
	"version":"2.1",
	"keyfrom":"fanyi.web",
	"action":"FY_BY_CLICKBUTTION",
	"typoResult":"false"
	}
	my_datas = urllib.parse.urlencode(FormateData).encode(encoding='UTF8')
	my_headers ={
		"Accept-Language": "zh-Hans-CN,zh-Hans;q=0.7,ja;q=0.3",
		"User-Agent": random.choice(UA_List_PC),
		"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		"Accept": "application/json, text/javascript, */*; q=0.01",
		"X-Requested-With": "XMLHttpRequest",
		"Content-Length": len(my_datas),
		"Host": "fanyi.youdao.com",
		"Connection": "Keep-Alive",
		"Pragma": "no-cache",
	}
	request  = urllib.request.Request (url,data = my_datas,headers = my_headers)
	text  = urllib.request.urlopen(request).read()
	target = json.loads(text.decode("UTF-8"))
	results = target['translateResult'][0][0]['tgt']
	return results
def BingTranslate(key):
	FormateData = {
	"q":key,
	"qs":"n",
	"form":"Z9LH5",
	"sp":"-1",
	"pq":key,
	"sc":"8-1",
	"sk":"",
	"cvid":"0FB337345A9443FABC342D4F520C1138"
	}
	my_datas = urllib.parse.urlencode(FormateData)

	url = "https://cn.bing.com/dict/search"+"?"+my_datas
	my_datas = urllib.parse.urlencode(FormateData).encode(encoding='UTF8')
	#my_datas = urllib.parse.urlencode(FormateData).encode(encoding='UTF8')
	my_headers ={
	"User-Agent": random.choice(UA_List_PC),
	}
	request  = urllib.request.Request (url,headers = my_headers)
	text  = urllib.request.urlopen(request).read()
	findText  = text.decode("UTF-8")
	#print(text.decode("UTF-8"))
	findText =findText[findText.find("必应词典为您提供"+key+"的释义，")+len("必应词典为您提供"+key+"的释义，"):]
	findText =findText[:findText.find(" /><meta")-1]
	#print(text.decode("UTF-8"))
	return findText
def is_english_char(ch):
    if ord(ch) not in (97,122) and ord(ch) not in (65,90):
        return False
    return True
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
	isEnglish =key.isalpha()
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
	print(key+"->"+results)
	return results


def PythonLocation():
	return os.path.dirname(os.path.realpath(__file__))

#XML特征
# <?xml version="1.0" encoding="UTF-8"?>
# <data>
#     <ref link="ability_damage_enemyfront_desc">
#         <string lang="en">Deals #value1# damage to the closest enemy</string>
#         <string lang="fr">Inflige #value1# de dégâts à l'ennemi le plus proche</string>
#         <string lang="it">Infligge #value1# di danno al nemico più vicino</string>
#         <string lang="de">Fügt dem Feind, der sich am wenigsten weit entfernt befindet, #value1# Schaden zu.</string>
#         <string lang="es">Provoca #value1# puntos de daños al enemigo más cercano.</string>
#         <string lang="pt">Causa #value1# de dano ao inimigo mais perto</string>
#     </ref>
# </data>
def TranslateXML(_ResourceLocation,_DesLocation):	
	if _ResourceLocation.find(".xml")!=-1:
		print("Translate xml Started:"+_ResourceLocation)
		file_object = open(_ResourceLocation,encoding="utf8")
		Context=[]
		try:
			all_the_text = file_object.readlines()
			for i in all_the_text:
				if i.find("lang=\"en\"")!=-1:#找到需要翻译的特征符合lang="en"
					text = i[i.find(">")+1:i.rfind("</")]
					TranslatedText = BingTranslateContext(text)
					TranslatedContext = i.replace(text,TranslatedText)
					Context.append(TranslatedContext.replace("lang=\"en\"","lang=\"zh-cn\""))#添加中文特征符合
					Context.append(i)
				else:
					Context.append(i)
		finally:
			file_object.close( )
		file_object_read = open(_DesLocation,'w',encoding="utf8")
		try:
			file_object_read.writelines(Context)
		finally:
			file_object_read.close()
	else:
		pass
def TranslateDoc(_ResourceLocation,_DesLocation):
	pass


def TranslateAllFolder():
	myList = ListFolder(PythonLocation())
	for i in myList:
		if i.find(".")!=-1:
			TranslateXML(PythonLocation()+"/"+i,PythonLocation()+"/TranslatedFileFolder/"+i)#翻译xml格式
			TranslateDoc(PythonLocation()+"/"+i,PythonLocation()+"/TranslatedFileFolder/"+i)#翻译doc格式

def main():
	TranslateAllFolder()
if __name__ == '__main__':
    main()