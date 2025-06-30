n=int(input("enter any no"))
print(n)
sum=0
while n>0:
    a=n%10
    sum=sum+a
    n=n//10
print(sum,type(sum))