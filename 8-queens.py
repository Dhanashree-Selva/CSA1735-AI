
N = 8
board = [-1] * N

def is_safe(row, col):
    for r in range(row):
        if board[r] == col:
            return False

        if abs(board[r] - col) == abs(r - row):
            return False

    return True

def solve(row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False

if solve(0):
    print("Solution:")
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution")
