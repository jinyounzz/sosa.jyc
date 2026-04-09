import sys
k, l = map(int, sys.stdin.readline().split())
waiting_list = {}
for i in range(l):
    student_id = sys.stdin.readline().strip()
    waiting_list[student_id] = i
sorted_list = sorted(waiting_list.items(), key=lambda x: x[1])
count = 0
for student_id, order in sorted_list:
    if count == k:
        break
    print(student_id)
    count += 1