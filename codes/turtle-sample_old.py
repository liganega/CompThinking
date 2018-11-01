import turtle as t

win = t.Screen()
tuti = t.Turtle()
tuti.shape("turtle")

# 함수 정의
def polygon(n):
    i = 0
    while i < n:
        tuti.forward(1000/n)
        tuti.left(360/n)
        i = i + 1

polygon(7)
tuti.lt(30)
polygon(5)
