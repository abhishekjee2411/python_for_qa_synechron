#Create a list of squares of odd numbers between 1 and 25

i=1
l=[]
while(i <= 25):
	l.append(i**2)
	i+=2
print(l)

m=[]
for i in range(1,26,2):	#allocating odd values to i, starting from 1 and going on till 25, like 1,3,5,......,25
	m.append(i**2)
print(m)