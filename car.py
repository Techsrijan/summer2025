from turtle  import *

import fontTools.feaLib.ast

t=Turtle()
t.speed(7)
sc=Screen()
sc.title('Car')
bgcolor('white')
sc.setup(1100,700)

t.penup()
t.right(90)
t.forward(200)
t.pendown()
t.right(90)
t.forward(200)
t.right(90)
t.circle(50,extent=180)
t.right(93.5)
t.forward(110)
t.right(80)
t.forward(10)
t.right(80)
t.forward(10)
t.left(70)
t.forward(80)
t.left(90)
t.forward(10)

t.circle(-5,extent=175)

t.left(10)
t.forward(100)
t.left(30)
t.forward(120)
t.right(42)
t.forward(320)
t.right(40)
t.forward(120)
t.left(37)
t.forward(200)
t.right(90)
t.forward(8)

t.left(80)
t.forward(3)
t.right(90)
t.forward(10)
t.right(80)
t.forward(3)

t.left(80)
t.forward(80)
t.circle(-5,extent=70)
t.forward(120)

t.right(90)
t.circle(50,extent=180)


t.right(99.5)
t.forward(150)




t.penup()
t.right(180)
t.forward(10)
t.left(85)
t.forward(10)

t.pendown()
t.left(8)
t.forward(190)
t.right(90)
t.forward(90)
t.right(40)
t.forward(60)
t.right(50)
t.forward(150)
t.right(90)
t.forward(138)


t.penup()
t.forward(20)
t.pendown()
t.forward(140)
t.right(90)
t.forward(110)
t.right(10)
t.forward(80.5)
t.right(80)
t.forward(127)
t.right(90)
t.forward(190)

t.penup()
t.right(90)
t.forward(250)
t.right(90)
t.forward(120)

t.pendown()
t.right(40)
t.forward(90)
t.right(50)
t.forward(50)
t.right(120)
t.forward(80)
t.right(60)
t.forward(69.5)
t.penup()
t.right(180)
t.forward(120)
t.pendown()
t.forward(125)
t.left(90)
t.forward(64)
t.left(90)
t.forward(112)
t.left(80)
t.forward(66)

t.penup()
t.left(100)
t.forward(159)
t.pendown()
t.forward(122)
t.left(90)
t.forward(30)
t.left(50)
t.forward(51)
t.left(40)
t.forward(84)
t.left(90)
t.forward(62)

t.penup()
t.forward(25)
t.pendown()
t.left(90)
t.pensize(6)
t.forward(13)

t.penup()
t.right(180)
t.forward(150)
t.pendown()
t.forward(15)

t.penup()
t.forward(115)
t.left(90)
t.forward(72)
t.left(90)
t.pensize(17)
t.pendown()
t.circle(-32)
t.penup()
t.right(90)
t.forward(12)
t.pendown()
t.pensize(5)
for i in range(5):
    t.fd(21)
    t.left(72)
    t.bk(20)


t.penup()
t.left(91)
t.forward(448)
t.pendown()
t.pensize(17)
t.circle(-32)

t.penup()
t.right(90)
t.forward(12)
t.pendown()
t.pensize(5)
for i in range(5):
    t.fd(21)
    t.left(72)
    t.bk(20)















# t.end_fill()




done()