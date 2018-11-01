import turtle

win = turtle.Screen()
tuti = turtle.Turtle()
tuti.shape("turtle")

angle = 1
step = 3

def halfLeaf():
    i = 0
    while i < 60:
        tuti.forward(step)
        tuti.right(angle)
        i = i + 1

    tuti.right(120)    

def leaf():
    j = 0
    while j < 2: 
        halfLeaf()
        j = j + 1

k = 0
while k < 6:
    leaf()
    tuti.left(60)
    k = k + 1






    



