import turtle

win = turtle.Screen()
tuti = turtle.Turtle()
tuti.shape("turtle")


### 꽃잎 반쪽 그리기
# count: 전진과 회전의 반복횟수
# angle * count가 180보다 작아야 반쪽 꽃잎을 그린다.
def halfLeaf(count, step, angle):
    for i in range(count):
        tuti.forward(step)
        tuti.right(angle)


### 꽃잎 그리기
# halfLeaf를 두 번 그리면 된다.
# 대신에 한 번 그릴 때마다 방향을 반대 방향으로 돌려야 한다.
def leaf(count, step, angle):
    for i in range(2):
        halfLeaf(count, step, angle)
        tuti.right(180 - count * angle)    # 반대 방향 바라보기
      
### 꽃잎 6장 꽃 그리기
# leaf 함수를 6번 사용하면 된다.
# 꽃잎을 하나 그릴 때마다 60도 회전시켜야 한다.
def flower(num, count, step, angle):
    for k in range(num):
        leaf(count, step, angle)
        tuti.left(360/num)

flower(7, 60, 6, 2)








#win.mainloop()
