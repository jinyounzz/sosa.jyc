#2490
for _ in range(3):
    yut = list(map(int, input().split()))
    count_zero = yut.count(0)
    if count_zero == 1:
        print('A') # 도
    elif count_zero == 2:
        print('B') # 개
    elif count_zero == 3:
        print('C') # 걸
    elif count_zero == 4:
        print('D') # 윷
    elif count_zero == 0:
        print('E') # 모
