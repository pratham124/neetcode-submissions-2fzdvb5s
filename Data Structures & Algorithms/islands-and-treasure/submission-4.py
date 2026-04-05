class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647 
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))

        visit = set()
        while q:
            for _ in range(len(q)):
                r, c, d = q.popleft()
                if (r, c) in visit:
                    continue
                visit.add((r, c))
                grid[r][c] = d
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or (nr, nc) in visit or grid[nr][nc] != INF:
                        continue
                    q.append((nr, nc, d + 1))
        



