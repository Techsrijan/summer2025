from numpy import *
arr=array([1,4,5,6,8,4,4,4,4,3,1,3])
print(arr)

arr2=arr.reshape(4,3)
print(arr2)
print(arr2.shape)
print(arr2.ndim)

arr3=arr2.flatten()
print(arr3)

a=array([1,2,3,4,6])
b=array([5,3,7,8])
print(concatenate((a,b)))

arr2d=array([
    [1,2,3,4],
    [4,5,6,4],
    [7,8,9,4],
    [5,5,6,4]

])
print(arr2d)

print(arr2d.ndim)
print(arr2d.shape)


arr2d1=array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [5,5,6],


])

#print(arr2d+arr2d1)
print(dot(arr2d,arr2d1))
print(arr2d@arr2d1)



