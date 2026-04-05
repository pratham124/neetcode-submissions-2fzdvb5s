class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ROWS = len(board)
        COLS = len(board[0])
        def dfs(r, c):
            board[r][c] = "T"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or board[nr][nc] != "O":
                    continue
                dfs(nr, nc)


        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == "O":
                    dfs(r, c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"
 
