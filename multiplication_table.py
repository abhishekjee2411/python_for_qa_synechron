for i in range(20):
	print("2 X",i,"=",str(2*i))

for x in range(1,6):
	print("------------------------------------------")
	for y in range(1,21):
		print("{} X {} = {}".format(x,y,x*y))
	print("------------------------------------------")
print ("Multiplication Table Ends!")


name="India"
age=70

print("Hello {}, you are {} years old".format(name,age))
print("Hello {1}, you are {0} years old".format(age,name))
print("Hello {1}, you are {0:f} years old".format(age,name))
print("Hello {1}, you are {0:3f} years old".format(age,name))