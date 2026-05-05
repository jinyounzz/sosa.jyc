import random

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)  # 매번 다른 판을 만들기 위해 숫자를 섞음
                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def is_valid(board, row, col, num):
    # 가로, 세로 체크
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    # 3x3 박스 체크
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def remove_numbers(board, count):
    """지정한 개수만큼 숫자를 지워 빈칸(.)으로 만듦"""
    while count > 0:
        r, c = random.randint(0, 8), random.randint(0, 8)
        if board[r][c] != 0:
            board[r][c] = 0
            count -= 1

def print_board(board):
    line = "-" * 25
    for i in range(9):
        if i % 3 == 0:
            print(line)
        row_str = "| "
        for j in range(9):
            val = board[i][j]
            row_str += (str(val) if val != 0 else ".") + " "
            if (j + 1) % 3 == 0:
                row_str += "| "
        print(row_str)
    print(line)

# 1. 빈 판 생성 및 완성된 스도쿠 만들기
board = [[0]*9 for _ in range(9)]
solve(board)

# 2. 난이도 조절 (숫자 40~50개 정도 지우기)
remove_numbers(board, 45)

# 3. 출력
print_board(board)