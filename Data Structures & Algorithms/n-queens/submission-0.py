class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        def is_valid(r, c):
            # Check same column
            i = r - 1
            while i >= 0:
                if board[i][c] == 'Q':
                    return False
                i -= 1

            # Check upper-left diagonal
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if is_valid(r, c):
                    board[r][c] = 'Q'
                    dfs(r + 1)
                    board[r][c] = '.'

        dfs(0)
        return res