# A set is an ordered set of unique elements

myfriends={"alam","madhav","modi","modi","sonia"}
print(myfriends)
mysistersfriends={"madhav","sonia","vijaya","hari"}
print(myfriends.union(mysistersfriends))
print(myfriends - mysistersfriends)
print(myfriends.intersection(mysistersfriends))

# You can use sets to remove duplicates from a list

l = [2,3,2,3,4,5,6,7,6,7,8,9,9,10]
print(l)
s = set(l)
print(s)
v = list(s)
print(v)
