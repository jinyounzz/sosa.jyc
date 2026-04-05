#3052
numbers = [int(input()) for i in range(10)]
remainder = [numbers[j]%42 for j in range(len(numbers))]
result_ = set(remainder)
print(len(result_))