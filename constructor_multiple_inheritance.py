class Theory:
    def __init__(self):
        print("This is theory")
    def t_marks(self):
        print('this is theory marks')

class Sessional:
    # def __init__(self):
    #     print("This is sessional")
    def s_marks(self):
        print('this is sessional marks')

class Result(Sessional,Theory):
    pass
    # def __init__(self):
    #     print("This is result")


r=Result()
