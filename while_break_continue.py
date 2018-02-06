while True:
	name=input("Enter your name:")
	if len(name) > 1:
		print("{} is a valid name".format(name))
		break

print("****************************************************")

while True:
	name=input("Enter your name:")
	if name == "name":
		print("Your name can't be name!")
		continue
	elif len(name) > 1:
		print("{} is a valid name".format(name))
		break
