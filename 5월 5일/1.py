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

def solve_operation():
    n = int(input("N을 입력하세요 (1 < N <= 5): "))

    A = create_random_matrix(n)
    B = create_random_matrix(n)
    C = create_random_matrix(n)

    print_matrix(A, "Matrix A")
    print_matrix(B, "Matrix B")
    print_matrix(C, "Matrix C")

    AB = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                AB[i][j] += A[i][k] * B[k][j]

    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = AB[i][j] + C[i][j]

    print_matrix(result, "Result (A x B + C)")

if __name__ == "__main__":
    solve_operation()