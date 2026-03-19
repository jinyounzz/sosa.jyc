#2455
current = 0
max_people = 0
for _ in range(4):
    out_p, in_p = map(int, input().split())
    current -= out_p
    current += in_p
    if current > max_people:
        max_people = current
print(max_people)
