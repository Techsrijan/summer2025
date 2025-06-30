class Student:
    def subject_name(self):
        print("Python Training")

    def school_name(self):
        print("Techsrijan")

    def add(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)

    # contructor is a special member function which will be
    # invocked auromatically when the object is created
    def __init__(self):   # constructor deafult
        print("Hum to bina object ke hi run karenge")
        self.p=50
        self.q=50

    def total(self):
        print(self.p+self.q)
ob=Student() # creating object(ob) of student class

#Student.subject_name(ob) # self is the object of that class
ob.school_name()
ob.subject_name()

ob1=Student() # # creating object(ob1) of student class

ob.add(4,5)
ob.total()