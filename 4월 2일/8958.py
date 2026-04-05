#8958
T = int(input())

for i in range(T):
    ox_result = input().strip()

    total_score = 0
    current_score = 0

    for j in ox_result:
        if j == 'O':
            current_score += 1
            total_score += current_score
        else:
            current_score = 0

    print(total_score)

