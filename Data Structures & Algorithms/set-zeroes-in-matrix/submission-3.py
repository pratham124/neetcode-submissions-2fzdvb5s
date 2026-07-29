class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstRow = firstCol = False
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r == 0:
                        firstCol = True
                    if c == 0:
                        firstRow = True
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if firstRow:
            for r in range(ROWS):
                matrix[r][0] = 0
        if firstCol:
            for c in range(COLS):
                matrix[0][c] = 0

                    