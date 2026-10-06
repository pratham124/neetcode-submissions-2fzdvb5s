class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(word)


        def dfs(r, c, i):
            if i == n - 1 and board[r][c] == word[i]:
                return True
            
            if board[r][c] != word[i]:
                return False
            
            cur_c = board[r][c]
            board[r][c] = "+"
            for d1, d2 in dirs:
                nr = r + d1
                nc = c + d2
                if nr < 0 or nr == ROWS or nc < 0 or nc == COLS:
                    continue
                
                if dfs(nr, nc, i + 1):
                    return True
            board[r][c] = cur_c
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False