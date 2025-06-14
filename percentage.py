a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=int(input("enter fourth number"))
e=int(input("enter fifth number"))
total=a+b+c+d+e
print("Total=",total)
per=total*100/500
print("percentage=",per)
if per<33:
    print("Fail")
elif per>=33 and per<45:
    print("third division")
elif per>=45 and per<60:
    print("second division")
elif per>=60:
    print("first division")
