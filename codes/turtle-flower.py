import turtle

win = turtle.Screen()
tuti = turtle.Turtle()
tuti.shape("turtle")

angle = 1
step = 3

### 꽃잎 반쪽 그리기
# count: 전진과 회전의 반복횟수
# angle * count가 180보다 작아야 반쪽 꽃잎을 그린다.
def halfLeaf(count):
    i = 0
    while i < count:
        tuti.forward(step)
        tuti.right(angle)
        i = i + 1

### 꽃잎 그리기
# halfLeaf를 두 번 그리면 된다.
# 대신에 한 번 그릴 때마다 방향을 반대 방향으로 돌려야 한다.
def leaf():
    i = 0
    while i < 2:
        halfLeaf(60)
        tuti.right(180 - 60 * angle)    # 반대 방향 바라보기
        i = i + 1

### 꽃잎 6장 꽃 그리기
# leaf 함수를 6번 사용하면 된다.
# 꽃잎을 하나 그릴 때마다 60도 회전시켜야 한다.
k = 0
while k < 6:
    leaf()
    tuti.left(60)
    k = k + 1

win.mainloop()
