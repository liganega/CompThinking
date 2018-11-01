import turtle

win = turtle.Screen()
tuti = turtle.Turtle()

# polygon 함수 정의
def polygon(n):
    i = 0

    while i < n:
        tuti.forward(100)
        tuti.left(360/n)
        i = i + 1

# 5각형 그리기
polygon(5)

# 이어서 그리는 도형이 겹치지 않도록 거북이를 반대방향으로 향하게 한다.
# 또한 도형을 구분하기 위해 펜의 색깔도 빨간색으로 변경한다.
tuti.left(180)
tuti.pencolor('red')

# 6각형 그리기
polygon(6)

win.mainloop()
