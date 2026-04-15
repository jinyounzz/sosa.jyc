#4673
def d(n):
    n = n + sum(map(int, str(n)))
    return n
not_self_numbers = set()
for i in range(1, 10001):
    generated_num = d(i)
    if generated_num <= 10000:
        not_self_numbers.add(generated_num)
for j in range(1, 10001):
    if j not in not_self_numbers:
        print(j)