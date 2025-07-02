'''
there are 3 types of method
1. instance method--by defalut argument self
2. class method
3. static method
'''
class Student:
    school_name="Techsrijan"
    def student_marks(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def get_total(self):
        return self.m1+self.m2+self.m3

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    @staticmethod   #decorator
    def msg():
        print("This will run with.class name")

Student.msg()
ob=Student()
ob.student_marks(50,60,70)
print(ob.get_total())
print(Student.get_school_name())

