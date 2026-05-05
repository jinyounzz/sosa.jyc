import random

def print_matrix(matrix, name):
    print(f"[{name}]")
    for row in matrix:
        for val in row:
            print(f"{val:>6}", end=" ")
        print()
    print("-" * 30)

def create_random_matrix(n):
    limit = n * n * 10
    return [[random.randint(1, limit - 1) for _ in range(n)] for _ in range(n)]

def solve_transpose():
    n = int(input("N을 입력하세요 (1 < N <= 5): "))

    target = create_random_matrix(n)
    print_matrix(target, "Original Matrix")

    transposed = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposed[j][i] = target[i][j]

    print_matrix(transposed, "Transposed Matrix")

if __name__ == "__main__":
    solve_transpose()