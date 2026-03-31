

N = int(input())
num = N
count = 0

while True:
    a = num // 10
    b = num % 10
    new_num = b * 10 + (a + b) % 10

    count += 1
    num = new_num

    if num == N:
        break

print(count)
