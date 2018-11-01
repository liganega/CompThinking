import turtle

win = turtle.Screen()
tuti = turtle.Turtle()
tuti.shape("turtle")

def polygon(n):
    i = 0

    while i < n:
        tuti.forward(1000/n)     # 전진 길이를 n에 의존하게 만듦
        tuti.left(360/n)
        i = i + 1

polygon(100)

win.mainloop()
