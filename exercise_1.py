a=["I","am","a","007","enthusiast"]
b=a.sort()
print(a)
print(b)
print(a[-1:])


c=[34,254,643,2,2348,43,321,46,4,45,98,3.45,5.6,23.56786]
d=c
print("List d is:",d)
c.sort()
print(c)
c.reverse()			#the reversal takes place in-place. The end-result cannot be captured, hence it cannot be transferred to another variable.
print(c)
f=c.pop()
print("Smallest value is:",str(f))

