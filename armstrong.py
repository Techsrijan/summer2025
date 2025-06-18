n=int(input("enter any no"))
print(n)
orig=n
sum=0
while n>0:
    a=n%10
    sum=sum+a*a*a
    n=n//10
print("sum=",sum)
if sum==orig:
    print("Armstrong no")
else:
    print("not armstrong")