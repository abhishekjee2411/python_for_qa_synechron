d={'H':'Hydrogen','O':'Oxygen'}
print(type(d))
print(d.keys())
print(d.values())
print(d.items())
print(d['H'])           #prints the value of the key 'H'
print(d.get('H'))       #prints the value of the key 'H' (the Java way)
d['C']='Carbon'         #inserting a new key-value pair ('C','Carbon')
print(d)
del(d['H'])             #deleting the key-value pair for the key 'H'
print(d)

#Dictionaries are useful in scenarios where there is need for a lookup