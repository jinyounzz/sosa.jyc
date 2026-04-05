#2750
n = int(input())
numbers = [int(input()) for i in range(n)]
numbers.sort()
for j in range(len(numbers)):
    print(numbers[j])