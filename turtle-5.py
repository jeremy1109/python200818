import turtle

a=turtle.Turtle()
turtle.shape("turtle")
n=int(input("輸入數字"))
for i in range(n):
    a.forward(100)
    a.left(360/n)
turtle.done()