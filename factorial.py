def factorial(n):
    if n<0:
        raise ValueError("Negative numbers do not have factorials!")
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
		
print(factorial(993))
