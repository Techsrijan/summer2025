a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
#nested if else
if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
elif(b>c):
    print(" B is greatest")
else:
    print("c is greatest")
