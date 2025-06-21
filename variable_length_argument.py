def addtotal(a,b,d):
    c=a+b+d
    print(c)

#addtotal(4,5,5)

#4. variable length argument (*)
def total(a,*b):
    sum=a
    for i in b:
        sum=sum+i
    return sum
    # print(a,type(a))
    # print(b,type(b))

print(total(1,3,7,7,434,434,6,2,5,2,5,5))


#4. variable length argument (*)
def total1(*b):
    sum=0
    for i in b:
        sum=sum+i
    return sum
    # print(a,type(a))
    # print(b,type(b))

print(total1(1,3,7,7,434,434,6,2,5,2,5,5))