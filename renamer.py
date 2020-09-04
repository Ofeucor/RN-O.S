#!/usr/bin/python3

import sys, os
from os import listdir
from os.path import isfile, join

def main(argv):
	try:
		for f in listdir(argv[0]): 
			if isfile(join(argv[0], f)):
				old_name = f.split(".")
				new_name = old_name[0] + argv[1] + "." + old_name[1]
				os.rename(join(argv[0], f), join(argv[0], new_name))
	except:
		print("Something went wrong, try again:\npython renamer.py \"<path>\" \"<suffix>\"\nrenamer.py \"<path>\" \"<suffix>\"")
		  
		# rename() function will 
		# rename all the files 
		#os.rename(src, dst)

if __name__ == "__main__":
	if "renamer.py" in sys.argv[0]:
		main(sys.argv[1:])
	else:
		main(sys.argv)
	sys.exit(0)