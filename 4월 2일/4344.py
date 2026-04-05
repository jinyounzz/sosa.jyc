#4344
import sys
C = int(sys.stdin.readline())
for _ in range(C):
    data = list(map(int, sys.stdin.readline().split()))
    N = data[0]         # 학생 수
    scores = data[1:]   # 점수 리스트
    avg = sum(scores) / N
    above_avg_count = 0
    for score in scores:
        if score > avg:
            above_avg_count += 1
    ratio = (above_avg_count / N) * 100
    print(f"{ratio:.3f}%")