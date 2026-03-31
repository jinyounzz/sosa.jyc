

N, K = map(int, input().split())

max_val = 0

for i in range(1, K + 1):
    num = N * i
    reversed_num = int(str(num)[::-1])
    max_val = max(max_val, reversed_num)

print(max_val)
