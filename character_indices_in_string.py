#write a function to print all the indices of a character in a string
# get_indices("banana","a") should return [1,3,5]

def get_indices(x,y):
	loc=[]
	
	c=0
	print(len(x))
	while (c<len(x)):
		if (x[c]==y):
			loc.append(c)
		c += 1

	return loc

loc = []
strng = input("Enter a string:")
charc = input("Enter the character to be searched:")
print(strng,"\t",charc)

loc = get_indices(strng,charc)
print("The character",charc,"is located in the string",strng,"at locations:",loc)
