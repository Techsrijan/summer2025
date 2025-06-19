from array import *
a=array('f',[1,4,5,6,8,4,4,4.0,4,3])
print(a)
for i in a:
    print(i)
print("Length of an arrat=",len(a))
print(a.count(4))
print(a.typecode)
print(a.buffer_info())
ch=array('u',['a','g'])
print(ch)
