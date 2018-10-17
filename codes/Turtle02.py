import turtle
win = turtle.Screen()

tuti = turtle.Turtle()
tuti.shape("turtle")        # 화살표 대신 거북이 모양 선택
tuti.pencolor("blue")       # 선 색깔을 blue로 지정

tuti.penup()                # 펜 들기 (이동할 때 선을 그리지 않게 됨)

size = 20                   # 전진 길이 지정

for i in range(30):
   tuti.stamp()             # 거북이 모양 도장 찍기
   size = size + 3          # 회전을 점차 크게 돌도록 만들기
   tuti.forward(size)       # size 크기만큼 전진하기
   tuti.right(24)           # 24도 우회전하기

win.mainloop()
