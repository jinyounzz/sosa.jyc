#2399
n = int(input())
x = list(map(int, input().split()))
x.sort()
result = 0
for j in range(len(x)):
    result += x[j] * (2 * j - 2 * (n - 1 - j))
print(result)