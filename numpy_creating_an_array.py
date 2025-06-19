'''
there are six ways to creating an array using numpy
1- array
2-linspace
3-logspace
4-arange
5-zeros
6-ones

'''
from numpy import *
#array
arr=array([33,5,6,4])
print(arr)

#linspace
arr2=linspace(1,15,3)  #bydefault50
print(arr2)

#logspace
arr3=logspace(1,15,3)
print(arr3)

#arange
arr4=arange(1,14,2)
print(arr4)

#zeros
arr5=zeros(10,int)
print(arr5)

#ones
arr6=ones(10)
print(arr6)