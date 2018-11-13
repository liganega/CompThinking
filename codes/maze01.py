import turtle
win = turtle.Screen()
win.bgpic("../images/maze01.png")

# 거북이 속성
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("blue")
t1.turtlesize(.7)
t1.penup()

# 속도조절
t1.speed(1)

# 마우스 클릭 이벤트 처리 함수
def mousegoto(x,y):
    print(x)
    t1.goto(x,y)

def keyforward():
    t1.forward(50)

print(t1.heading())

# 이벤트 처리
win.onclick(mousegoto)
win.onkey(keyforward, "Right")


win.listen()
turtle.mainloop()
