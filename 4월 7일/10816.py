#10816
import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))
count_dict = Counter(cards)
print(*(count_dict[target] for target in targets))