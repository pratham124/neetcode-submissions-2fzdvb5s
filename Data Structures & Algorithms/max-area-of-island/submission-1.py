class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != 1):
                return 0
            grid[r][c] = 0
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            cur_area = 1
            for x, y in dirs:
                nr = r + x
                nc = c + y
                cur_area += dfs(nr, nc)
            return cur_area




        for r in range(ROWS):
            for c in range (COLS):
                max_area = max(dfs(r, c), max_area)
        return max_area