#2530
h, m, s = map(int, input().split())
d = int(input())
total_seconds = h * 3600 + m * 60 + s + d
new_h = (total_seconds // 3600) % 24
new_m = (total_seconds // 60) % 60
new_s = total_seconds % 60
print(new_h, new_m, new_s)
