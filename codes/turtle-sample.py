import turtle as t

win = t.Screen()
tuti = t.Turtle()
tuti.shape("turtle")

def polygon(n):
    i = 0

    while i < n:
        tuti.forward(1000/n)
        tuti.left(360/n)
        i = i + 1

polygon(100)
tuti.pencolor('red')
polygon(50)
