#2581
import sys

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

primes = []

for i in range(m, n + 1):
    if is_prime(i):
        primes.append(i)

if not primes:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))