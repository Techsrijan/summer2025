n=int(input("enter any no"))
print(n)
orig=n
rev=0
while n>0:
    a=n%10
    rev=rev*10+a
    n=n//10
print("reverse=",rev)
if rev==orig:
    print("Palindrome no")
else:
    print("not Palindrome")