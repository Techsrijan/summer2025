# reading contents from file
# f=open("areoplane.txt","r")
# print(f)
#print(f.read())
#print(f.readline(25))
#print(f.readlines(10))

# for data in f:
#     print(data,end='')


#writing contents to file
#f=open("apple.txt","w")
f=open("apple2.txt","a")
print(f)
s=input("enter any text u want to write")
f.write(s)
f.close()


f=open("apple2.txt","r")
for i in f:
    print(i)