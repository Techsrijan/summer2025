from math import *
def add(p,q):
    c=p+q
    print("Output=",c)

add(55,66)


def sub(x,y):
    d=x-y
    return d

s=sub(15,8)
print("sub=",s)

print("Sqare root of 36=",sqrt(36))

def calci(s,t):
    a=s+t
    b=s-t
    c=s*t
    d=s/t
    return a,b,c,d

sum,sub,mul,div=calci(40,5)
print(sum,sub,mul,div)