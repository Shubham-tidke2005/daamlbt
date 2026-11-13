
def solve(board, row, n):

    if row == n:
        return True

    for col in range(n):
        safe = True

        for i in range(row):
            for j in range(n):
                if board[i][j] == 1:
                    if j == col or abs(i-row) == abs(j-col):
                        safe = False

        if safe:
            board[row][col] = 1

            if solve(board, row+1, n):
                return True

            board[row][col] = 0

    return False


n = int(input("Enter number of queens: "))

board = [[0] * n for i in range(n)]

if solve(board, 0, n):
    print("N-Queens Matrix:")
    for row in board:
        print(*row)
else:
    print("No solution")
