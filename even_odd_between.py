# a=int(input("enter Any number"))
# if a%2==0:
#     print("even no")
# else:
#     print("Odd no")


start=int(input("enetr start no"))
last=int(input("enetr last no"))
print("start=",start,"last=",last)

if start<last:
    i=start
    while i<=last:
        if i % 2 == 0:
            print("even no=",i)
        else:
            print("Odd no=",i)
        i=i+1
else:
    i = start
    while i >= last:
        if i % 2 == 0:
            print("even no=", i)
        else:
            print("Odd no=", i)
        i = i - 1














