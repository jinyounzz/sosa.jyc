# 2153.py

word = input().strip()

total = 0

for ch in word:
    if 'a' <= ch <= 'z':
        total += ord(ch) - ord('a') + 1
    else:
        total += ord(ch) - ord('A') + 27

def is_prime(n):
    if n == 1:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(total):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
