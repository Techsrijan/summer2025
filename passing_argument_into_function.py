'''
passing an agument to function
1. positional argument
2. keyword argument
3. default argument
4. variable length argument (*)
5. keyword variable length argumnent
'''
#1. positional argument

def person(name,age,status='single',gender='male'):
    print("name=",name)
    age=age+10
    print("age=",age)
    print("status",status)
    print("gender=",gender)

person('ashwani',66)
#person(55,'ram')

#2. keyword argument
person(name="ram",age=55)
person(age=45,status='married',name='rohan')

#3. default argument