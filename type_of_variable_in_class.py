'''
there are two type of variable in a class
1. instance variable --varibale declared inside function
2. class variable
'''
'''
Class variables are defined within the class construction. Because they are owned by the class itself, class variables are shared by all instances of the class. They therefore will generally have the same value for every instance unless you are using the class variable to initialize a variable.

Defined outside of all the methods, class variables are, by convention, typically placed right below the class header and before the constructor method and other methods.
'''

'''
Instance Variables
Instance variables are owned by instances of the class. This means that for each object or instance of a class, the instance variables are different.

Unlike class variables, instance variables are defined within methods.

'''
class Car:
    wheel=4   # class variable
    def __init__(self):  #deafult
        self.mil=25
        self.compnay="maruti"

    def print_wheel(self):
        print(self.wheel)

c1=Car()
c2=Car()
print(c1.mil,c1.compnay,c1.wheel)
c2.mil=50
#Car.mil=800
Car.wheel=6
# print(c1.mil,c1.compnay,c1.wheel)
print(c2.mil,c2.compnay,c2.wheel)
print(c1.mil,c1.compnay,c1.wheel)
#
# c1.print_wheel()