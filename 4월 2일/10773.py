#10773
k = int(input())
numbers = []
for _ in range(k):
    num = int(input())
    if num == 0:
        numbers.pop()
    else:
        numbers.append(num)
print(sum(numbers))