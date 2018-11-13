import turtle
win = turtle.Screen()
win.bgpic('maze01.png')

t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("red")
t1.turtlesize(0.7)
t1.penup()
t1.speed(1)



# 마우스 클릭 할 때 
def mousegoto(x,y):
    t1.goto(x,y)

# 방향키 누를 때

step = 5

def keyforward():
    old_x, old_y = t1.pos()
    t1.goto(old_x + step, old_y)
    
def keybackward():
    old_x, old_y = t1.pos()
    t1.goto(old_x - step, old_y)

def keyupward():
    old_x, old_y = t1.pos()
    t1.goto(old_x, old_y + step)

def keydownward():
    old_x, old_y = t1.pos()
    t1.goto(old_x, old_y - step)

# 이벤트 처리 
win.onclick(mousegoto)
win.onkey(keyforward, "Right")
win.onkey(keybackward, "Left")
win.onkey(keyupward, "Up")
win.onkey(keydownward, "Down")

win.listen()







