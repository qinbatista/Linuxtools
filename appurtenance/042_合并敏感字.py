import sys
import os
import platform
def PythonLocation():
	return os.path.dirname(os.path.realpath(__file__)).replace("\\","/")
import os
import sys
import time
import json
import random
import requests
import calendar
import shutil
import xml.etree.ElementTree as ET
import sys
import subprocess
import xml.dom.minidom
from pathlib import Path as PathLib

class TextMergeManager(object):

	def __init__(self):
		self.__new_words_list = []
		self.__old_words_list = []

	def _read_context(self, _path):
		with open(_path,encoding="utf8") as file_object:
			text_content=[]
			text_content = file_object.readlines()
		return text_content

	def _write_context(self,_path,_content):
		with open(_path,mode='w',encoding="utf8") as file_context:
			file_context.writelines(_content)

	def _read_unformatted_txt(self,_path):
		text_content = self._read_context(_path)
		for line in text_content:
			new_line = line.replace(" ","")
			new_line = new_line.strip()
			if new_line == "\n" or new_line =="":
				continue
			word_list = new_line.split("，")
			self.__new_words_list = self.__new_words_list + word_list
		return self.__new_words_list

	def _read_formatted_txt(self, _path):
		self.__old_words_list = self._read_context(_path)
		return self.__old_words_list

	def _merge_text(self):
		for line in self.__new_words_list:
			if line not in self.__old_words_list:
				self.__old_words_list.append(line+"\n")
			else:
				print("have line="+line)

	def start_merge(self,new_text, old_text):
		self._read_unformatted_txt(new_text)
		self._read_formatted_txt(old_text)
		self._merge_text()
		self._write_context(old_text,self.__old_words_list)

def main():
	sam = TextMergeManager()
	sam.start_merge("/Users/batista/Desktop/aaa.txt","/Users/batista/Desktop/sensitivewords.txt")



if __name__ == '__main__':
    main()