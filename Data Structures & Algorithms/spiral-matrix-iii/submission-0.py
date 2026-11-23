class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:


        row, col = rStart, cStart
        res = [[row, col]]
        step = 1

        while len(res) < rows * cols:

            # East
            for _ in range(step):
                col += 1
                if 0 <= row < rows and 0 <= col < cols:
                    res.append([row, col])

            # South
            for _ in range(step):
                row += 1
                if 0 <= row < rows and 0 <= col < cols:
                    res.append([row, col])

            step += 1

            # West
            for _ in range(step):
                col -= 1
                if 0 <= row < rows and 0 <= col < cols:
                    res.append([row, col])

            # North
            for _ in range(step):
                row -= 1
                if 0 <= row < rows and 0 <= col < cols:
                    res.append([row, col])

            step += 1

        return res

