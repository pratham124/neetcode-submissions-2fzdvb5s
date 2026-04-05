class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
            
        pacific_q = deque()
        atlantic_q = deque()
        ROWS = len(heights)
        COLS = len(heights[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    pacific_q.append((r, c))
                if r == ROWS - 1 or c == COLS - 1:
                    atlantic_q.append((r, c))
        
        def bfs(q):
            res = [[False for _ in range(COLS)] for _ in range(ROWS)]
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    res[r][c] = True
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr == ROWS or nc < 0 or nc == COLS or res[nr][nc] or heights[nr][nc] < heights[r][c]:
                            continue
                        q.append((nr, nc))
            return res


        pac = bfs(pacific_q)
        atl = bfs(atlantic_q)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res