import sys
n, m = map(int, sys.stdin.readline().split())
unheard = set()
for _ in range(n):
    unheard.add(sys.stdin.readline().strip())
unseen = set()
for _ in range(m):
    unseen.add(sys.stdin.readline().strip())
result = list(unheard & unseen)
result.sort()
print(len(result))
for name in result:
    print(name)