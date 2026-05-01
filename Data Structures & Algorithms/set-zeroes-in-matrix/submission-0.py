class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)          # Number of rows
        n = len(matrix[0])       # Number of columns

        first_row_zero = False   # Flag for first row
        first_col_zero = False   # Flag for first column

        # Step 1: Check if first row has any zeros
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Step 2: Check if first column has any zeros
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Step 3: Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark row
                    matrix[0][j] = 0  # Mark column

        # Step 4: Zero out cells based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 5: Zero out first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Step 6: Zero out first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0