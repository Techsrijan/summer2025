from turtle import *
t=Turtle() # creating obejct of turtle class
# t2=Turtle()
j=['red','green','blue','orange','yellow']
t.pensize(5)
for i in range(1000):
    t.pencolor(j[i%5])

    t.forward(i%500)
    t.left(100)
# t2.pensize(5)
# for i in range(1000):
#     t2.pencolor(j[i%5])
#
#     t2.forward(i%500)
#     t2.left(100)
done()