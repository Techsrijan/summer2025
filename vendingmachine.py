n=int(input("How many toffe u want"))
print(" you want=",n,"toffee")
stock=15
i=1
while i<=n:
    if i<=stock:
        print("Collect toffe=",i)

    else:
        print("Out Of stock")
        break
    i=i+1
else:
    print("thank u please visit again")