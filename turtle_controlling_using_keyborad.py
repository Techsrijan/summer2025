from turtle import *
t=Turtle() # creating obejct of turtle class
t.speed(1)  # help('turtle.speed')
t.shape('turtle') #help('turtle.shape')
sc=Screen()
sc.listen()

def moveFd():
    t.fd(100)

def moveBk():
    t.bk(100)

def turnLeft():
    t.left(90)

def turnRight():
    t.right(90)

sc.onkey(moveFd,'X')
sc.onkey(moveBk,'Down')
sc.onkey(turnLeft,'Left')
sc.onkey(turnRight,'Right')
done()