#1065
import sys

def is_hansu(n):
    if n < 100:
        return True
    nums = list(map(int, str(n)))
    if (nums[1] - nums[0]) == (nums[2] - nums[1]):
        return True
    return False
N = int(sys.stdin.readline())
count = 0
for i in range(1, N + 1):
    if is_hansu(i):
        count += 1

print(count)