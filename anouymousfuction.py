def add(x,y):
    return(x+y)

def is_even(n):
    return n%2==0

print(is_even(10))
print(add(5,6))
'''
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.
'''

f=lambda a,b:a+b
print(f(100,20))

