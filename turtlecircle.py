from turtle import *
t=Turtle() # creating obejct of turtle class
t.circle(100) #anticlockwise
t.circle(-100) #clockwise
#.clear()
t.undo()
t.goto(100,100)
def sq():
    t.forward(100)
    t.left(90)
for i in range(4):
    sq()
t.reset()
def sq1():
    t.forward(200)
    t.left(90)
for i in range(4):
    sq1()
t.reset()    
t.circle(100)
t.goto(0,100)
t.pencolor('blue')
for i in range(25):
    t.forward(100)
    t.backward(100)
    t.left(15)

done()