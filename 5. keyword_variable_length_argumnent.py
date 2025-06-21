#5. keyword variable length argumnent
def persondata(**data):
    print(data)
    for i in data.items():
        print(i)

persondata(name='ashwani',age=55,city='gkp',phone=9956477677,quali='btech')