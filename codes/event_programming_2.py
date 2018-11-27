'''
이벤트 기반 프로그래밍
* 사용자 또는 컴퓨터에서 발생하는 이벤트에 반응하는 방식을 프로그래밍하기
* 이벤트가 언제 발생할 지 모르므로 상시 대기해야 함
* 게임 등을 프로그래밍 할 때 활용
* 필요 요소
  - 이벤트 정의
  - 이벤트와 이벤트 처리 함수 연결하기
  - 이벤트 입력 장치 준비 및 설정하기
  - 프로그램이 종료될 때까지 무한대기 시키기

* 거북이 그래픽의 이벤트 프로그램
  - 1단계: 캔버스, 거북이 생성 등 기본적인 화면 구성하기
  - 2단계: 이벤트 정하기
    + 마우스 클릭 및 키보드 버튼 누르기
  - 3단계: 이벤트가 발생할 경우 처리하는 함수 만들기
  - 4단계: 이벤트와 처리 함수 연결하기
  - 5단계: 이벤트 무한대기
'''

# 1단계
import turtle
win = turtle.Screen()
win.bgpic("maze1.png")

t1 = turtle.Turtle()
t1.shape('turtle')
t1.color('red')
t1.penup()
t1.speed(3)  # 거북이 이동 속도 지정

# 2단계

## 클릭 이벤트
## 방향키 이벤트: 동, 서, 남, 북 4개

# 3단계

## 클릭 이벤트 처리 함수
def mousegoto(x, y):
    t1.goto(x,y)
    if isInTrap():
        turtle.bye()
    

step = 10

## 방향기 이벤트 처리 함수
def keyeast():
    t1_x, t1_y = t1.pos()
    t1.goto(t1_x + step, t1_y)
    if isInTrap():
        turtle.bye()

def keywest():
    t1_x, t1_y = t1.pos()
    t1.goto(t1_x - step, t1_y)
    if isInTrap():
        turtle.bye()

def keysouth():
    t1_x, t1_y = t1.pos()
    t1.goto(t1_x, t1_y - step)
    if isInTrap():
        turtle.bye()

def keynorth():
    t1_x, t1_y = t1.pos()
    t1.goto(t1_x, t1_y + step)
    if isInTrap():
        turtle.bye()

# 종료이벤트
def exitProgram():
    turtle.bye()

def keyend():
    t1.home()

# 4단계

## 클릭 이벤트 처리 연동
win.onclick(mousegoto)

## 방향키 이벤트 처리 연동
win.onkey(keyeast, "Right")
win.onkey(keywest, "Left")
win.onkey(keysouth, "Down")
win.onkey(keynorth, "Up")

## 종료 이벤트 처리 연동
win.onkey(exitProgram, 'q')
win.onkey(exitProgram, 'Q')
win.onkey(keyend, 'e')
win.onkey(keyend, 'E')

# 함정 직사각형의 좌표
x1 = 110
y1 = -115

x2 = 135
y2 = -140

# 함정 색깔 지정
t1.fillcolor("red")

t1.begin_fill()
t1.goto(x1, y1)
t1.pendown()
t1.goto(x2, y1)
t1.goto(x2, y2)
t1.goto(x1,y2)
t1.goto(x1,y1)
t1.end_fill()

t1.penup()
t1.home()

# 거북이가 함정에 빠진다는 사실 구현
# 거북이와 함정의 좌표 활용

def isInTrap():
    x0, y0 = t1.pos()
    if x1 <= x0 <= x2 and y2 <= y0 <= y1:
        return True
    else:
        return False


# 5단계
win.listen()

win.mainloop()  # X 버튼이 눌릴 때 까지 살아 있음
























    































