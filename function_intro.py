#function definition with no argument
def greet():
    print("good morning")

greet()  #function

def add(x,y): # here x and y are called fromal argument
    c=x+y
    print("Add=",c)

add(2,3)
a=int(input("enter any number"))
b=int(input("Enetr and number"))
add(a,b) # here a and b are called actual argument
# when we call any function the value of actual argument copied
# into formal argument
greet()


x=int(input("enter any number"))
y=int(input("Enetr and number"))
add(x,y)