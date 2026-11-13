
class Solution:

    def isvalid(self, board, row, col, n):

        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper left diagonal
        i = row - 1
        j = col - 1

        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check upper right diagonal
        i = row - 1
        j = col + 1

        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def nQueen(self, board, ans, row, n):

        if row == n:
            ans.append(["".join(r) for r in board])
            return

        for j in range(n):
            if self.isvalid(board, row, j, n):
                board[row][j] = 'Q'

                self.nQueen(board, ans, row + 1, n)

                board[row][j] = '.'

    def solveNQueens(self, n):

        board = [['.'] * n for i in range(n)]
        ans = []

        self.nQueen(board, ans, 0, n)

        return ans


n = int(input("Enter number of queens: "))

obj = Solution()
result = obj.solveNQueens(n)

if result:
    print("N-Queens Solutions:")
    for solution in result:
        for row in solution:
            print(row)
        print()
else:
    print("No solution")
