import turtle
 

a=turtle.Turtle()

b=turtle.Turtle()
a.color("blue")
b.color("red")
a.pensize(10)
a.pensize(5)
for i in range(360):
    a.forward(1)
    a.right(1)
    b.forward(1)
    b.left(1)
