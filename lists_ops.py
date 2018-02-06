a=[1,5,8,3,5,9,7]
print(type(a))
print(a[0])
print(a[-1])
print(len(a))
print(sum(a))
print(min(a))
print(max(a))
print(a[2:5])
print(a[::2])

print("---------------------------Methods applicable on a list---------------------------")
a=[1,5,8,3,5,9,7]
a.append(9)
print(a)
a.insert(1,200)
print(a)
print(a.index(5))   #always prints the index of the first occurrence of "5"
print(a.count(5))   #always prints the number of occurrences of "5"
a.sort()
print(a)
a.reverse()
print(a)
a.remove(9)         #removes the first occurrence of "9"
print(a)
c=a.pop()
print(c)
print(a)
a.extend([7,8,9])
print(a)
