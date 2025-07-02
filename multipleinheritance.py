class Theory:
    def t_marks(self):
        print('this is theory marks')

class Sessional:
    def s_marks(self):
        print('this is sessional marks')

class Result(Theory,Sessional):
    pass

r=Result()
r.t_marks()
r.s_marks()