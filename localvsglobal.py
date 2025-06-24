x=50 #global vairable
def test():
    global z
    z=600
    x=200
    y=10  #local variable
    print("Local y=",y)
    print("x=", x)
    print("z=",z)
    d=globals()['x']
    print("accessing global over local=",d)

test()
print(x)
print("Local to global=",z)