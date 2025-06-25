from turtle import *
t=Turtle() # creating obejct of turtle class
# t.pu()
# t.fd(100)
# t.left(90)
# t.fd
t.goto(100,100)
# t.pd()
t.pencolor('#1514ce')
def sq():
    t.forward(100)
    t.left(90)
for i in range(4):
    sq()
t.backward(200)
done()