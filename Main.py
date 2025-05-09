import os
import time

def main():
	os.system("clear")
	print("e to edit, r to run x to exit")
	input1 = input()
	if input1 == "e":
		os.system("dir")
		print("Path/")
		path = input()
		command = "sudo nano " + path
		os.system(command)
		main()

	if input1 == "r":
		os.system("dir")
		print("Path/")
		path = input()
		command = "python3 " + path
		os.system(command)
		time.sleep(3)
		main()
	
	if input1 == "x":
		print("bye")
		time.sleep(1)

main()
