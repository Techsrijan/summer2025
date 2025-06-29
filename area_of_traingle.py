from math import *
a=int(input("Enter first side of trangle"))
b=int(input("Enter second side of trangle"))
c=int(input("Enter third side of trangle"))
s=(a+b+c)/2
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("Area=",area)