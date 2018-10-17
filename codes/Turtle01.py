import turtle

win = turtle.Screen()
tuti = turtle.Turtle()
tuti.shape('turtle')

n = 6

i = 0
while i < n:
    tuti.forward(150)
    tuti.left(360/n)
    i = i + 1

win.mainloop()
