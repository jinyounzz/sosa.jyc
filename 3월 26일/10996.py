

import sys

N = int(sys.stdin.readline())

line1 = ""
for i in range(N):
    if i % 2 == 0:
        line1 += "*"
    else:
        line1 += " "

line2 = ""
for i in range(N):
    if i % 2 == 0:
        line2 += " "
    else:
        line2 += "*"

for i in range(2 * N):
    if i % 2 == 0:
        print(line1)
    else:
        print(line2)
