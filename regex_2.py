import sys
import re

if len(sys.argv) == 3:
	pattern = sys.argv[1]
	filename = sys.argv[2]
else:
	pattern = input("Enter pattern")
	filename = input("Enter filename")
	
f=open(filename,'r')

for lineno,line in enumerate(f):
	if re.search(pattern,line):
		print(lineno + 1,line.rstrip())

#close the file
f.close()