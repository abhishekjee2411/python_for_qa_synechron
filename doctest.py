import doctest

def sub(a,b):
	"""
>>> sub(4,5)
-1
>>> sub(9,0)
9
>>> sub(0,0)
0
    """
	return a-b

doctest.testmod()