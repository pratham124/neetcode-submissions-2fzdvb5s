class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        parent = [n for n in range(ROWS * COLS)]
        rank = [1] * (ROWS * COLS)

        def index(r, c):
            return r * COLS + c

        def find(n):
            cur = n
            while cur != parent[cur]:
                parent[cur] = parent[parent[cur]]
                cur = parent[cur]
            return cur

        def union(n1, n2):
            f1 = find(n1)
            f2 = find(n2)

            if f1 == f2:
                return False

            if rank[f1] > rank[f2]:
                parent[f2] = f1
                rank[f1] += rank[f2]
            else:
                parent[f1] = f2
                rank[f2] += rank[f1]
            return True
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    islands += 1

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr < 0 or nc < 0 or nr >= ROWS or
                            nc >= COLS or grid[nr][nc] == "0"
                        ):
                            continue
                        if union(index(r, c), index(nr, nc)):
                            islands -= 1

        return islands