import time
import os
cmd = input("input your cmd:")
while cmd=="":
	cmd = input("input your cmd:")
while True:
	os.system(cmd)
	print("try again")
	time.sleep(5)
