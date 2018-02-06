#Unpacking

a=b=c=2
print(a,b,c)
#	2 2 2
a,b,c=2,3,4
print(a,b,c)
#	2 3 4
a=[4,5,6]
x,y,z=a			#Assignment of list values to the variables, serially (unpacking)
print(x,y,z)	
#	4 5 6
print(a)
#	[4, 5, 6]
x,y,z=a
print(x)
#	4
print(y)
#	5
print(z)
#	6
w,x,y,z=a
#Traceback (most recent call last):
#  File "<pyshell#141>", line 1, in <module>
#    w,x,y,z=a
#ValueError: not enough values to unpack (expected 4, got 3)
	
	#The error above cropped up because there were not enough values to fill up the assigned variables.