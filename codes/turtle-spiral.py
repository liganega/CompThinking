import turtle

win = turtle.Screen()
tuti = turtle.Turtle()
tuti.shape("turtle")

tuti.penup()
tuti.stamp()

### 소용돌이 그리기 ###
# 걸음걸이: step에서 3씩 증가
# 회전각도: angle
# 도장찍기 반복 회수: count
def spiral(step,angle,count):
    i = 0
    while i < count:
        tuti.forward(step + 3 * i)
        tuti.stamp()
        tuti.right(angle)
        i = i + 1

# 첫 걸음걸이 20, 회전각도 30, 반복횟수 40을 지정하여
# 소용돌이 그리기
spiral(20,30,40)

win.mainloop()
