def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

print(fact(5))

def fact1(n):
    f=1
    for i in range(n,0,-1):
        f=f*i
    print(f)
fact1(5)
