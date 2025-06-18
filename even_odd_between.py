# a=int(input("enter Any number"))
# if a%2==0:
#     print("even no")
# else:
#     print("Odd no")


start=int(input("enetr start no"))
last=int(input("enetr last no"))
print("start=",start,"last=",last)
sum_even=0
sum_odd=0
if start<last:
    i=start
    while i<=last:
        if i % 2 == 0:
            print("even no=",i)
            sum_even=sum_even+i
        else:
            print("Odd no=",i)
            sum_odd=sum_odd+i
        i=i+1
else:
    i = start
    while i >= last:
        if i % 2 == 0:
            print("even no=", i)
            sum_even = sum_even + i
        else:
            print("Odd no=", i)
            sum_odd = sum_odd + i
        i = i - 1

print("sum of even no=",sum_even)
print("sum of odd no=",sum_odd)












