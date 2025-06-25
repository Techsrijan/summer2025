from turtle import *
t=Turtle() # creating obejct of turtle class
sc=Screen()
sc.setup(1000,800)
sc.title("My Graphics")
# sc.bgcolor('yellow')
sc.bgpic('test.gif')
t.pencolor('#1514ce')
def sq():
    t.forward(100)
    t.left(90)
for i in range(4):
    sq()
done()