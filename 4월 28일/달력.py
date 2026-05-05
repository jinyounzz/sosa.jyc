# 달력
month = int(input()) # 월 받기
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 매월 마지막 날짜
start_day = 4 # 올해 1월 1일은 목요일이므로

# 시작 일 계산하기
total_days = 0 # 1월부터 N월까지 일수 더하기
for i in range(month - 1):
    total_days += days[i]
first_day = (start_day + total_days) % 7

print("      ", month, "월") # 달력 출력 시작
print(" 일 월 화 수 목 금 토")

print("   " * first_day, end="") # 요일 공백 잡기

count = first_day # 토요일에 끊기게

for j in range(1, days[month - 1] + 1): # 1일부터 N일까지
    if j < 10:
        print("", j, end="") # 한자리 숫자 공백
    else:
        print(j, end="")
    count += 1 # 토요일에 끊기게
    if count % 7 == 0: # 카운트가 7의 배수이면 줄바꿈
        print()
    else:
        print(" ", end="") # 숫자 뒤에 공백
        