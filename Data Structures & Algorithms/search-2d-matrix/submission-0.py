class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rowNum = -1
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = l + (r-l) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                rowNum = m
                break
            elif matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        
        if rowNum == -1:
            return False

        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            m = l + (r - l) // 2

            if matrix[rowNum][m] == target:
                return True
            elif matrix[rowNum][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
        