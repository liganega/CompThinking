# A와 B 두 사라람이 숫자 맛추기 게임하기

# A
secret = 5

# B
guess = 0

while secret != guess:
    guess = int(input("숫자를 맞수세요! "))
    if secret == guess:
        print("맞았습니다")
    else:
        if secret < guess:
            print("너무 커요")
        else:
            print("너무 작아요")
        
