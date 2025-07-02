'''
deriving a new class(child class) from the base class (parent class)
is known as inheritacnce.
it provides the concept of code resability.
'''
class Room:  #parent class
    def area(self,l,b):
        self.l=l
        self.b=b
        print("area=",self.l*self.b)

class Guest_room(Room):  #child class
    def msg(self):
        print("this is guest room")



g=Guest_room()
g.area(55,33)
g.msg()

# r=Room()
# r.msg()