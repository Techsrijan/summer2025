# f=open("apple.txt",'r')
# f2=open("ship.txt",'w')
#
# for data in f:
#     f2.write(data)
#
# f.close()
# f2.close()

image=open("test.gif","br")
myimage=open("rest.gif","bw")
for data in image:
    print(data)
    myimage.write(data)