from numpy import *
arr=array([1,4,5,6,8,4,4,4.0,4,3])
print(arr)
print(arr.dtype)
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(len(arr))

for i in arr:
    print(i,'',end='')

print()
print(arr[3:])
print(arr[1:8:2])

print(arr+5)

print(sort(arr))


