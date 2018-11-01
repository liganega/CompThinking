import turtle

win = turtle.Screen()
tuti = turtle.Turtle()
tuti.shape("turtle")

tuti.penup()
tuti.stamp()

i = 0
while i < 50:
    tuti.forward(10 + 3* i)
    tuti.stamp()
    tuti.right(30)
    i = i + 1
    
