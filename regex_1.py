import sys
import re

pattern = sys.argv[1]
filename = sys.argv[2]

f=open(filename,'r')

for lineno, line in enumerate(f):
	if re.search(pattern,line):
		print(lineno + 1,line.rstrip())

#close file
f.close()