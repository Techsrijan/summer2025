from numpy import *
arr=array([1,4,5,6,7])
print(arr,"arrress of arr=",id(arr))
arr2=arr  # aliasing
print(arr2,"arrress of arr2=",id(arr2))

arr2[0]=5000
print(arr2,"arrress of arr2=",id(arr2))
print(arr,"arrress of arr=",id(arr))
'''
changing in one array affects another and address remains same
'''


# we want if we change in one array it  affect another but
# the address is different
print('we want if we change in one array it  affect another but he address is different')
arr3=array([1,4,5,6,7,5,45])
print(arr3,"arrress of arr=",id(arr3))
arr4=arr3.view()  #shallow copy
print(arr4,"arrress of arr2=",id(arr4))

arr4[0]=1000
print(arr4,"arrress of arr4=",id(arr4))
print(arr3,"arrress of arr3=",id(arr3))


# we want if we change in one array it  does not affect another but
# the address is different

print('we want if we change in one array it  does not affect another but the address is different')
arr5=array([1,4,5,65,7,45,45])
print(arr5,"arrress of arr=",id(arr5))
arr6=arr5.copy() #deep copy
print(arr6,"arrress of arr6=",id(arr6))

arr5[0]=600
print(arr5,"arrress of arr5=",id(arr5))
print(arr6,"arrress of arr6=",id(arr6))